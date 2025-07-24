import json
import os
from typing import List, Dict, Any, Union, Tuple
from tqdm import tqdm
# from dafault_prompt import (DEFAULT_SYSTEM_PROMPT, DEFAULT_USER_PROMPT_FOR_ADDITIONAL_FUNCTION_FC, DEFAULT_USER_PROMPT_FOR_ADDITIONAL_FUNCTION_PROMPTING)
# from openai.types.chat.chat_completion_message_tool_call import ChatCompletionMessageToolCall

def read_dataset(dataset):
    
    input_querty_path = "data/" + dataset + ".json"
    input_answer_path = "data/possible_answer/" + dataset + ".json"

    with open(input_querty_path, 'r') as f:
        querry_list = list()
        for line in f:
            if line.strip():  # 确保不是空行
                try:
                    item = json.loads(line)
                    querry_list.append(item)
                except json.JSONDecodeError as e:
                    print(f"Error parsing line: {e}")
                    continue

    with open(input_answer_path, 'r') as f:
            answer_list = list()
            for line in f:
                if line.strip():  # 确保不是空行
                    try:
                        item = json.loads(line)
                        answer_list.append(item)
                    except json.JSONDecodeError as e:
                        print(f"Error parsing line: {e}")
                        continue
    return querry_list, answer_list

def get_arguments_type(schema: dict) -> type:
    """
    Recursively processes a JSON schema-like dictionary and returns the corresponding
    Python typing object.

    Args:
        schema: A dictionary representing the type schema.

    Returns:
        The Python type (e.g., str, List[int], Dict[str, Any]).
    """
    # 获取当前层级的类型
    schema_type = schema.get("type")

    # --- 递归的基准情形 (Base Cases) ---
    if schema_type == "string":
        return str
    if schema_type == "integer":
        return int
    if schema_type == "float":
        return float
    if schema_type == "boolean": # 为完整性添加布尔类型
        return bool
    
    # --- 递归步骤 (Recursive Steps) ---
    
    # 1. 处理列表 (array)
    if schema_type == "array" or schema_type == "list":
        # 获取列表内元素的类型定义
        items_schema = schema.get("items", {})
        # 递归调用，获取列表内元素的具体类型
        item_type = get_arguments_type(items_schema)
        return List[item_type]
    
    if schema_type == "tuple":
        items_schema = schema.get("items", {})
        # 递归调用，获取列表内元素的具体类型
        item_type = get_arguments_type(items_schema)
        return Tuple[item_type]

    # 2. 处理字典 (dict)
    if schema_type == "dict":
        properties = schema.get("properties", {})
        # 如果没有 'properties'，则将其视为一个任意键值的字典
        if not properties:
            return Dict[str, Any]
        
        # 递归获取所有子属性的类型
        # 使用集合来存储所有不同值的类型，自动处理重复
        value_types = {get_arguments_type(prop_schema) for prop_schema in properties.values()}
        
        # 如果所有子属性的类型都相同，则无需使用 Union
        if len(value_types) == 1:
            value_type = value_types.pop()
        else:
            # 如果有多种不同的类型，则使用 Union 联合它们
            value_type = Union[tuple(value_types)]
        
        return Dict[str, value_type]

    # 如果没有找到任何已知类型，则返回 Any 作为备用
    return Any

def get_parameter_type_map(schema: dict) -> Dict[str, type]:
    """
    获取顶层参数的名称到其类型的映射字典。
    
    Args:
        schema: 'parameters'部分的schema定义。

    Returns:
        一个字典，键是参数名(str)，值是其对应的Python类型(type)。
    """
    type_map = {}
    # 获取所有属性的定义
    properties = schema.get("properties", {})
    
    # 遍历每一个属性 (也就是你的变量)
    for param_name, param_schema in properties.items():
        # 使用之前的递归函数来解析这个属性的具体类型
        param_type = get_arguments_type(param_schema)
        # 将 "变量名" 和 "类型" 存入字典
        type_map[param_name] = param_type
        
    return type_map

def format_type(type_obj: type) -> str:
    """
    将一个类型对象格式化为简洁的字符串。
    - 处理 <class 'int'> 为 'int'
    - 处理 typing.List 为 'List'
    """
    # 对于 int, str, float 等内置类型，它们有 __name__ 属性
    # 并且它们的 __origin__ 属性不存在或为 None
    if hasattr(type_obj, '__origin__') and type_obj.__origin__ is not None:
        # 处理 typing.List, typing.Dict, typing.Union 等复杂类型
        return str(type_obj).replace('typing.', '')
    elif hasattr(type_obj, '__name__'):
        # 处理 int, str, float 等简单内置类型
        return type_obj.__name__
    else:
        # 备用方案，处理其他可能的情况
        return str(type_obj).replace('typing.', '')

def convert_schema_to_invocation(querry, answer, dataset):
    """
    将描述函数定义的输入格式，转换为描述函数调用的目标格式。

    由于输入格式缺少参数的具体值，该函数将在相应位置使用占位符。

    Args:
        input_data_list (list): 一个包含多个函数定义和对应问题的字典列表。

    Returns:
        dict: 结构转换后的字典，包含一个含有多个轮次的对话。
    """
    if not querry or not answer or len(querry) == 0 or len(answer) == 0:
        return {}

    # 从第一个输入项获取ID来生成场景信息
    base_id = querry.get("id", "generated")
    
    # 准备输出字典的基本结构
    output_structure = {
        "scenario": f"{base_id}",
        "module": f"scenarios.{dataset}.{base_id}",
        "conversations": [
            {
                "id": f"{base_id}_conversation",
                "turns": []
            }
        ]
    }

    # 遍历输入列表中的每一项，将其转换为一个 "turn"
    querry_item = querry
    answer_item = answer
    # 1. 提取用户查询
    try:
        input_prompt = querry_item["question"][0][0]["content"]
    except (KeyError, IndexError):
        input_prompt = ""

    answer_calls = []
    for func in answer_item.get("ground_truth", None):
        answer_calls.append(list(func.keys())[0].replace('.', '_'))  # 替换点号为下划线以创建有效的函数名
        

    
    # 2. 构建预期函数调用列表
    expected_calls = []
    for answer_fuc in answer_item["ground_truth"]:
        for k,v in answer_fuc.items():
            func_schema = get_data_by_function_name(querry_item.get("function", {}),k)
            arguments_list = []
            required = False
            function_name_answer = func_schema.get("name", "")
            function_name = function_name_answer.replace('.', '_')  # 替换点号为下划线以创建有效的函数名
            # 遍历函数定义的参数
            try:
                parameter_map = get_parameter_type_map(func_schema.get("parameters", {}))

                for param_name, param_details in func_schema.get("parameters", {}).get("properties", {}).items():
                    param_required = False
                    if param_name in func_schema["parameters"]["required"]:
                        param_required = True
                    # 这里是关键点：输入格式没有提供参数的值
                    # 我们用一个占位符来表示这个值需要从 query 中提取
                    # if param_name=='func' or param_name=='function':
                    #     output_structure["conversations"] = None
                    #     return output_structure
                    arguments_list.append({
                        "name": param_name,
                        "value": v[param_name], 
                        "type": format_type(parameter_map[param_name]),
                        "required": param_required
                    })
            except Exception as e:
                print(f"{e}")
                pass
        

        if function_name in answer_calls:
            required = True
        else:
            required = False
        
        call = {
            "name": function_name,
            "required": required,  
            "arguments": arguments_list
        }
        if required == True:
            expected_calls.append(call)
        else:
            # print(f"function {function_name} is not required")
            pass

    # 3. 组合成一个完整的 turn
    turn = {
        "query": input_prompt,
        "expected_function_calls": expected_calls
    }
    output_structure["conversations"][0]["turns"].append(turn)

    return output_structure

def get_data_by_function_name(data_list, function_name):
    for item in data_list:
        if isinstance(item, dict) and item.get('name') == function_name:
            return item
    return None

def generate_functions_from_json(data, output_filename):
    """
    从JSON数据生成Python函数文件。

    Args:
        data (str): 包含函数定义的JSON字符串。
        output_filename (str): 要保存生成的Python代码的文件名。
    """
    # try:
    #     tools = json.loads(data)
    # except json.JSONDecodeError as e:
    #     print(f"JSON 解析错误: {e}")
    #     return
    tools = data  # 假设 data 已经是一个有效的列表格式，不需要再解析

    with open(output_filename, 'w', encoding='utf-8') as f:
        tool_list = "["
        for tool in tools:
            # 将点号替换为下划线以创建有效的函数名
            func_name = tool['name'].replace('.', '_')
            tool_list += func_name + ", "
            func_description ="\t\"\"\"\n" + f"\t{func_name} : " + tool.get("description", '')
            func_description += """    
\tParameters:
"""
            
            params = tool.get('parameters', {})
            properties = params.get('properties', {})
            required_params = params.get('required', [])
            parameter_map = get_parameter_type_map(tool.get("parameters", {}))
            
            # 分离必需参数和可选参数
            args = []
            kwargs = []
            
            for param_name, param_details in properties.items():
                func_description += "\t" + param_name
                func_description += " (" + format_type(parameter_map[param_name]) + ")"
                func_description += ": " + param_details.get('description', '') + "\n"
                if param_name in required_params:
                    args.append(param_name+ ":" + format_type(parameter_map[param_name]))
                else:
                    # 使用 repr() 来获取默认值的正确字符串表示
                    default_value = repr(param_details.get('default'))
                    default_value_type = format_type(parameter_map[param_name])
                    kwargs.append(f"{param_name}:{default_value_type}={default_value}")
                    # TODO recorrect the type of default_value
            
            func_description += "\n\tRequired Parameter = ["
            for rp in required_params:
                func_description += rp
                func_description += ","
            func_description += "]\n"

            # 将必需参数放在前面
            all_params = ", ".join(args + kwargs)
            func_description += "\n\t\"\"\"\n"
            # 写入函数定义
            f.write("from typing import List, Dict, Any, Union, Tuple, Set \n")
            f.write(f"def {func_name}({all_params}):\n")
            f.write(f"{func_description}")
            f.write("\t" + "return 'Success'\n\n")
            
        tool_list = tool_list.rstrip(", ") + "]\n"
        f.write(f"tools = {tool_list}")
            
    # print(f"代码已成功生成并保存到 '{output_filename}' 文件中。")

if __name__ == "__main__":
    datasets = ["BFCL_v3_simple","BFCL_v3_parallel","BFCL_v3_parallel_multiple","BFCL_v3_multiple"]
    for dataset in datasets:
        querry_list, answer_list = read_dataset(dataset)
        output_path = "./scenarios/" + dataset + "/"
        if not os.path.exists(output_path):
            print(f"目录 '{output_path}' 不存在，正在创建...")
            os.makedirs(output_path)
            print("目录创建成功。")
        scenario_list = list()
        for i in tqdm(range(len(querry_list))):
            converted_output = convert_schema_to_invocation(querry_list[i],answer_list[i],dataset)
            scenario_list.append(converted_output)
        # print(json.dumps(converted_output, indent=2, ensure_ascii=False))

        file_path = "BFCL_v3_simple_ground_truth.json"
        file_path = "./scenarios/" + dataset + "_ground_truth.json"

        with open(file_path, 'w', encoding='utf-8') as f:
            # 4. 使用 indent 和 ensure_ascii 参数
            json.dump(scenario_list, f, indent=4, ensure_ascii=False)

        # print(f"列表已成功存入美化格式的文件: {file_path}")

        for i in range(len(querry_list)):
            print(f"Processing query {i+1}/{len(querry_list)}")
            output_filename = output_path + f"{querry_list[i]['id']}.py"
            generate_functions_from_json(querry_list[i].get("function", []), output_filename = output_filename)
