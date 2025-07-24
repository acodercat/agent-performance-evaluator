import asyncio
import json
from adapters.llama_index_agent_adapter import LLamaIndexAgentFactory
from llama_index.llms.openai_like import OpenAILike
from evaluation import evaluate
import os

file_names = []
file_names.append("./scenarios/BFCL_v3_simple_ground_truth.json")
file_names.append("./scenarios/BFCL_v3_multiple_ground_truth.json")
file_names.append("./scenarios/BFCL_v3_parallel_ground_truth.json")
file_names.append("./scenarios/BFCL_v3_parallel_multiple_ground_truth.json")

async def process_and_evaluate_llamaindex(file_name: str, semaphore: asyncio.Semaphore):
    async with semaphore:
    
        with open(file_name, 'r', encoding='utf-8') as f:
            ground_truths = json.load(f)

        model_id = "deepseek-v3-0324"
        api_key = "sk-bJL4pRKdjSZFMCd727AeB7Fd79Fe4eBaBaD41cA033BfB282"
        base_url = "https://oneapi.hkgai.net/v1"
    

        llm = OpenAILike(
            model=model_id,
            api_base=base_url,
            api_key=api_key,
            is_chat_model=True,
            is_function_calling_model=True
        )
        agent_factory = LLamaIndexAgentFactory(llm)

        os.makedirs("./results/"+ model_id + "_results/", exist_ok=True)
        
        output_file = file_name.replace("./scenarios/","./results/"+ model_id + "_results/")
        output_file = output_file.replace("_ground_truth","_" + model_id + "_results_llamaindex")
        
        await evaluate(agent_factory, ground_truths, output_file)

async def main():

    max_concurrent_tasks = 1
    semaphore = asyncio.Semaphore(max_concurrent_tasks)
    tasks = [process_and_evaluate_llamaindex(file_name, semaphore) for file_name in file_names]
    
    await asyncio.gather(*tasks)

    print("all tasks is done")

if __name__ == "__main__":
    asyncio.run(main())