import json

def load_json_stream(file_path):
    """
    读取一个包含多行JSON对象或一个JSON数组的文件。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip().startswith('['):
                return json.loads(content)
            else:
                # 尝试处理多行JSON对象
                file_content = content.replace('}\n{', '},{')
                json_array_string = f"[{file_content}]"
                return json.loads(json_array_string)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # 如果第一种方式失败，尝试按行解析
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return [json.loads(line) for line in f if line.strip()]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"解析文件 '{file_path}' 时出错: {e}")
            return None

def analyze_scenarios_by_id(file1_path, file2_path):
    """
    以 scenario ID 为基准进行匹配和分析，并记录仅存在于单一文件中的案例ID。
    """
    data1 = load_json_stream(file1_path)
    data2 = load_json_stream(file2_path)

    if data1 is None or data2 is None:
        return None

    scenarios_f1 = {s['scenario']: s for s in data1}
    scenarios_f2 = {s['scenario']: s for s in data2}

    all_scenario_ids = set(scenarios_f1.keys()) | set(scenarios_f2.keys())
    
    # 初始化统计器
    f1_total = len(scenarios_f1)
    f2_total = len(scenarios_f2)
    f1_success = 0
    f2_success = 0
    both_failed = 0
    both_success = 0
    f1_only_ids = []
    f2_only_ids = []

    def is_success(scenario_data):
        return all(not turn.get('validation_errors') 
                   for conv in scenario_data.get('conversations', []) 
                   for turn in conv.get('turns', []))

    for sid in all_scenario_ids:
        scenario1 = scenarios_f1.get(sid)
        scenario2 = scenarios_f2.get(sid)

        in_f1 = scenario1 is not None
        in_f2 = scenario2 is not None

        s1_success = in_f1 and is_success(scenario1)
        s2_success = in_f2 and is_success(scenario2)

        # 统计成功数
        if s1_success:
            f1_success += 1
        if s2_success:
            f2_success += 1

        # 统计独有ID
        if in_f1 and not in_f2:
            f1_only_ids.append(sid)
        elif not in_f1 and in_f2:
            f2_only_ids.append(sid)
        # 统计共同情况
        elif in_f1 and in_f2:
            if not s1_success and not s2_success:
                both_failed += 1
            elif s1_success and s2_success:
                both_success += 1

    return {
        "file1_path": file1_path,
        "file2_path": file2_path,
        "f1_total": f1_total,
        "f2_total": f2_total,
        "f1_success": f1_success,
        "f2_success": f2_success,
        "both_success": both_success,
        "both_failed": both_failed,
        "total_unique_scenarios": len(all_scenario_ids),
        "f1_only_ids": sorted(f1_only_ids),
        "f2_only_ids": sorted(f2_only_ids),
    }

# --- 主程序 ---
# 将模型版本作为可调整的变量
model_version = "qwen2.5-coder-32b-instruct" 

file_pairs = {
    "Multiple": (f"{model_version}_results/BFCL_v3_multiple_{model_version}_results_llamaindex.json", f"{model_version}_results/BFCL_v3_multiple_{model_version}_results.json"),
    "Parallel": (f"{model_version}_results/BFCL_v3_parallel_{model_version}_results_llamaindex.json", f"{model_version}_results/BFCL_v3_parallel_{model_version}_results.json"),
    "Parallel Multiple": (f"{model_version}_results/BFCL_v3_parallel_multiple_{model_version}_results_llamaindex.json", f"{model_version}_results/BFCL_v3_parallel_multiple_{model_version}_results.json"),
    "Simple": (f"{model_version}_results/BFCL_v3_simple_{model_version}_results_llamaindex.json", f"{model_version}_results/BFCL_v3_simple_{model_version}_results.json")
}

overall_unique_scenarios = 0
overall_success_f1 = 0
overall_success_f2 = 0
overall_f1_total = 0
overall_f2_total = 0

category_results = {} # 用于存储每个分类的结果

# 遍历每一对文件并打印分析结果
for group_name, (file1, file2) in file_pairs.items():
    results = analyze_scenarios_by_id(file1, file2)
    if results:
        # 累加总体统计
        overall_unique_scenarios += results['total_unique_scenarios']
        overall_success_f1 += results['f1_success']
        overall_success_f2 += results['f2_success']
        overall_f1_total += results['f1_total']
        overall_f2_total += results['f2_total']

        category_results[group_name] = {
            "f1_total": results['f1_total'],
            "f2_total": results['f2_total'],
            "f1_success": results['f1_success'],
            "f2_success": results['f2_success'],
            "both_success": results['both_success'],
            "both_failed": results['both_failed'],
            "f1_only_ids": results['f1_only_ids'],
            "f2_only_ids": results['f2_only_ids'],
        }

# --- 打印格式化的结果 ---
print(f"模型版本: {model_version}")
print("\n---")
print("### 详细分类结果 ###")
output_order = ["Simple", "Multiple", "Parallel", "Parallel Multiple"]

for category in output_order:
    if category in category_results:
        res = category_results[category]
        print(f"**{category}**:")
        print(f"  文件1 (LlamaIndex) 成功: {res['f1_success']}/{res['f1_total']}")
        print(f"  文件2 (原始) 成功: {res['f2_success']}/{res['f2_total']}")
        # print(f"  共有 {res['both_success']} 个案例在两个文件中都成功。")
        # print(f"  共有 {res['both_failed']} 个案例在两个文件中都失败。")
        if res['f1_only_ids']:
            print(f"  文件1独有案例 ({len(res['f1_only_ids'])} 个): {res['f1_only_ids']}")
        if res['f2_only_ids']:
            print(f"  文件2独有案例 ({len(res['f2_only_ids'])} 个): {res['f2_only_ids']}")
        print("---")

# --- 打印总体统计结果 ---
print("\n### 总体统计结果 ###")
print(f"文件1 (LlamaIndex) 总案例数: {overall_f1_total}")
print(f"文件2 (原始) 总案例数: {overall_f2_total}")
print(f"两个文件中总的唯一案例数: {overall_unique_scenarios}")
print(f"整体成功数 (文件1 - LlamaIndex): {overall_success_f1}/1000")
print(f"整体成功数 (文件2 - 原始): {overall_success_f2}/1000")

# 计算并打印整体成功率
overall_accuracy_f1 = (overall_success_f1 / overall_f1_total * 100) if overall_f1_total > 0 else 0
overall_accuracy_f2 = (overall_success_f2 / overall_f2_total * 100) if overall_f2_total > 0 else 0

print(f"整体成功率 (文件1 - LlamaIndex): {overall_accuracy_f1:.2f}%")
print(f"整体成功率 (文件2 - 原始): {overall_accuracy_f2:.2f}%")