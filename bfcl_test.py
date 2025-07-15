import asyncio
from adapters.py_calling_agent_adapter import PyCallingAgentFactory
from py_calling_agent.models import LiteLLMModel
from evaluation import evaluate
import json

file_names = []
file_names.append("./scenarios/BFCL_v3_simple_ground_truth.json")
file_names.append("./scenarios/BFCL_v3_multiple_ground_truth.json")
file_names.append("./scenarios/BFCL_v3_parallel_ground_truth.json")
file_names.append("./scenarios/BFCL_v3_parallel_multiple_ground_truth.json")

# Load test scenarios
async def process_and_evaluate(file_name: str, semaphore: asyncio.Semaphore):
    async with semaphore:

        with open(file_name, 'r', encoding='utf-8') as f:
            ground_truths = json.load(f)

        # Create agent factory
        model = LiteLLMModel(
            model_id="deepseek-v3-0324",
            api_key="sk-bJL4pRKdjSZFMCd727AeB7Fd79Fe4eBaBaD41cA033BfB282",
            base_url="https://oneapi.hkgai.net/v1",
            custom_llm_provider='openai'
        )
        agent_factory = PyCallingAgentFactory(model)

        output_file = file_name.replace("./scenarios/","./results/")
        output_file = output_file.replace("_ground_truth","_results")
        # Run evaluation
        await evaluate(agent_factory, ground_truths, output_file)

async def main():
    """
    主函数，创建并并发运行所有文件的评估任务。
    """

    max_concurrent_tasks = 1  # 控制最大并发协程数
    semaphore = asyncio.Semaphore(max_concurrent_tasks)

    # 为列表中的每个文件创建一个协程任务
    tasks = [process_and_evaluate(file_name, semaphore) for file_name in file_names]
    
    # 使用 asyncio.gather 并发运行所有任务并等待它们全部完成
    await asyncio.gather(*tasks)
    
    print("all tasks is done")

if __name__ == "__main__":
    asyncio.run(main())