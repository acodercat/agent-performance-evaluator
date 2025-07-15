import asyncio
import json
from adapters.llama_index_agent_adapter import LLamaIndexAgentFactory
from llama_index.llms.openai_like import OpenAILike
from evaluation import evaluate

file_names = []
file_names.append("./scenarios/BFCL_v3_simple_ground_truth.json")
file_names.append("./scenarios/BFCL_v3_multiple_ground_truth.json")
file_names.append("./scenarios/BFCL_v3_parallel_ground_truth.json")
file_names.append("./scenarios/BFCL_v3_parallel_multiple_ground_truth.json")

async def process_and_evaluate_llamaindex(file_name: str, semaphore: asyncio.Semaphore):
    async with semaphore:
    
        # 1. 加载测试场景
        with open(file_name, 'r', encoding='utf-8') as f:
            ground_truths = json.load(f)

        # 2. 为每个任务创建独立的 LLM 和 Agent Factory 实例
        llm = OpenAILike(
            model="deepseek-v3-0324",
            api_base="https://oneapi.hkgai.net/v1",
            api_key="sk-bJL4pRKdjSZFMCd727AeB7Fd79Fe4eBaBaD41cA033BfB282",
            is_chat_model=True,
            is_function_calling_model=True
        )
        agent_factory = LLamaIndexAgentFactory(llm)
        
        # 3. 准备输出文件路径
        output_file = file_name.replace("./scenarios/", "./results/")
        output_file = output_file.replace("_ground_truth", "_llamaindex_results")
        
        # 4. 执行评估
        await evaluate(agent_factory, ground_truths, output_file)

async def main():
    """
    主函数，创建并并发运行所有文件的评估任务。
    """

    max_concurrent_tasks = 1  # 控制最大并发协程数
    semaphore = asyncio.Semaphore(max_concurrent_tasks)
    # 为列表中的每个文件创建一个协程任务
    tasks = [process_and_evaluate_llamaindex(file_name, semaphore) for file_name in file_names]
    
    # 使用 asyncio.gather 并发运行所有任务并等待它们全部完成
    await asyncio.gather(*tasks)

    print("all tasks is done")

# 运行主协程
if __name__ == "__main__":
    asyncio.run(main())