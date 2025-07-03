import json
import os
import importlib
from tqdm import tqdm
from core.evaluator import AgentEvaluator


async def evaluate(agent_factory, ground_truths, results_file):
    existing_results = {}
    if os.path.exists(results_file):
        with open(results_file, 'r') as f:
            existing_results = json.load(f)
    # Initialize evaluator with the agent factory
    evaluator = AgentEvaluator(agent_factory)
    # Run evaluation
   
    for ground_truth in tqdm(ground_truths, desc="Evaluating scenarios"):
        scenario_module = importlib.import_module(ground_truth['module'])
        scenario_name = ground_truth['scenario']
        if scenario_name in existing_results:
            print(f"Skipping already evaluated scenario: {scenario_name}")
            continue
        results = await evaluator.evaluate(scenario_name, scenario_module, ground_truth['conversations'])
        metrics = results['metrics']
        print(scenario_name, metrics)
        existing_results[scenario_name] = results
        with open(results_file, 'w') as f:
            json.dump(existing_results, f, indent=2)