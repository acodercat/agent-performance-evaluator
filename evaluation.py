import json
import logging
import os
import importlib
from tqdm import tqdm
from core.evaluator import AgentEvaluator



async def evaluate(agent_factory, ground_truths, results_file):

    logger = logging.getLogger(results_file)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    handler = logging.FileHandler(results_file, mode='a', encoding='utf-8', delay=False)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    completed_scenarios = set()
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    try:
                        result_obj = json.loads(line)
                        if not isinstance(result_obj, dict):
                            break
                        if 'scenario' in result_obj:
                            completed_scenarios.add(result_obj['scenario'])
                    except TypeError:
                        print("wrong type result_obj")
                    except json.JSONDecodeError:
                        print(f"Warning: Found a line in the results file that cannot be parsed: {line.strip()}")
                    except Exception as e:
                        print(f"failed，error: {e}")


    except FileNotFoundError:
        print("Results file not found, a new file will be created.")

    evaluator = AgentEvaluator(agent_factory)
   
    for ground_truth in tqdm(ground_truths, desc="Evaluating scenarios"):
        if not ground_truth:
            continue
        try:
            scenario_name = ground_truth['scenario']
            
            # 使用 set 进行高效的状态检查
            if scenario_name in completed_scenarios:
                # print(f"Skipping already evaluated scenario: {scenario_name}") # 可以取消注释来显示跳过信息
                continue

            if not ground_truth["conversations"]:
                logger.info(json.dumps({"scenario": scenario_name, "error": "conversations is not exist"}))
                continue

            # 导入模块并执行评估
            scenario_module = importlib.import_module(ground_truth['module'])
            results = await evaluator.evaluate(scenario_name, scenario_module, ground_truth['conversations'])
            
            # 在结果中加入 scenario_name 以便恢复状态
            results['scenario_name'] = scenario_name
            
            # --- 4. 简化和修正的写入逻辑 ---
            # 只写入刚刚完成的这一个结果，而不是遍历任何东西
            try:
                # json_string = json.dumps(results, indent=2, ensure_ascii=False)
                json_string = json.dumps(results, ensure_ascii=False)
                logger.info(json_string)
                handler.flush()
                
                # 更新内存中的状态
                completed_scenarios.add(scenario_name)
                
                # 打印实时指标
                print(f"completed: {scenario_name}, metric: {results.get('metrics', 'N/A')}")

            except Exception as e:
                logging.info(json.dumps({"scenario": scenario_name, "error": f"processing '{scenario_name}' failed，error: {e}"}))
                handler.flush()
                
        except Exception as e:
            # 捕获评估过程中的任何其他错误
            scenario_name_for_error = ground_truth.get('scenario', 'unknown scenario')
            
            logging.info(json.dumps({"scenario": scenario_name_for_error, "Serious error": f"evaluate '{scenario_name_for_error}'  Serious error: {e}"}))
            handler.flush()
            continue