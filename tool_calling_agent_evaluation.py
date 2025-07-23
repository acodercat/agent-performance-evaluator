from llama_index.llms.openai_like import OpenAILike
from llama_index.llms.anthropic import Anthropic
from adapters.llama_index_agent_adapter import LLamaIndexAgentFactory
from adapters.litellm_adapter import LitellmAgentFactory
from adapters.litellm_adapter import LitellmModel
from adapters.openai_agent_adapter import OpenAIAgentFactory
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
import asyncio
import json
from evaluation import evaluate 
from utils import load_model_config

ground_truths = json.load(open("./scenarios/ground_truths.json"))

async def evaluate_qwen3_2():
    model_config = load_model_config("qwen3")
    model = OpenAILike(
        model=model_config['model_id'],
        api_base=model_config['base_url'],
        api_key=model_config['api_key'],
        is_function_calling_model=True,
        is_chat_model=True
    )
    agent_factory = LLamaIndexAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/tool_calling_agent_qwen3_2.json")


async def evaluate_qwen3_3():
    model_config = load_model_config("qwen3")
    model = LitellmModel(
        model_id=model_config['model_id'],
        api_key=model_config['api_key'],
        base_url=model_config['base_url'],
        provider="openai"
    )
    agent_factory = LitellmAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/tool_calling_agent_qwen3_3.json")

async def evaluate_qwen3():
    model_config = load_model_config("qwen2-5-7b")
    model = OpenAIChatCompletionsModel(
        model=model_config['model_id'], 
        openai_client=AsyncOpenAI(base_url=model_config['base_url'], api_key=model_config['api_key'])
    )
    agent_factory = OpenAIAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/tool_calling_agent_qwen3.json")

async def evaluate_claude_3_7_sonnet():
    model_config = load_model_config("claude-3-7-sonnet-20240229")
    model = Anthropic(**model_config)
    agent_factory = LLamaIndexAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/tool_calling_agent_claude_3_7_sonnet.json")


if __name__ == "__main__":
    asyncio.run(evaluate_qwen3_3())
    # asyncio.run(evaluate_qwen3())