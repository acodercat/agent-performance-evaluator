from llama_index.llms.openai import OpenAI
from llama_index.llms.anthropic import Anthropic
from adapters.llama_index_agent_adapter import LLamaIndexAgentFactory
import asyncio
import json
from evaluation import evaluate 
from utils.model_loader import load_model_config

ground_truths = json.load(open("./scenarios/ground_truths.json"))

async def evaluate_gpt_4o():
    model_config = load_model_config("gpt-4o")
    model = OpenAI(**model_config)
    agent_factory = LLamaIndexAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/tool_calling_agent_gpt_4o.json")

async def evaluate_claude_3_7_sonnet():
    model_config = load_model_config("claude-3-7-sonnet-20240229")
    model = Anthropic(**model_config)
    agent_factory = LLamaIndexAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/tool_calling_agent_claude_3_7_sonnet.json")


if __name__ == "__main__":
    asyncio.run(evaluate_gpt_4o())
    # asyncio.run(evaluate_claude_3_7_sonnet())