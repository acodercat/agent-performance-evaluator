import asyncio
import json
from adapters.py_calling_agent_adapter import PyCallingAgentFactory
from py_calling_agent.models import LiteLLMModel
from evaluation import evaluate
from utils import load_model_config

ground_truths = json.load(open("./scenarios/ground_truths.json"))

async def evaluate_deepseek_v3():
    # Create a specific agent factory
    model_config = load_model_config("deepseek-v3-0324")
    model = LiteLLMModel(**model_config, custom_llm_provider='openai')
    agent_factory = PyCallingAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/py_calling_agent_deepseek_v3.json")

async def evaluate_gpt_4o():
    # Create a specific agent factory
    model_config = load_model_config("gpt-4o")
    model = LiteLLMModel(**model_config, custom_llm_provider='openai')
    agent_factory = PyCallingAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/py_calling_agent_gpt_4o.json")

async def evaluate_claude3_7_sonnet():
    # Create a specific agent factory
    model_config = load_model_config("claude-3-7-sonnet-20240229")
    model = LiteLLMModel(**model_config, custom_llm_provider='anthropic')
    agent_factory = PyCallingAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/py_calling_agent_claude3_7_sonnet.json")

async def evaluate_claude3_5_sonnet():
    # Create a specific agent factory
    model_config = load_model_config("claude-3-5-sonnet-20241022")
    model = LiteLLMModel(**model_config, custom_llm_provider='anthropic')
    agent_factory = PyCallingAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/py_calling_agent_claude3_5_sonnet.json")

async def evaluate_qwen2_5_72b():
    # Create a specific agent factory
    model_config = load_model_config("qwen2-5-72b")
    model = LiteLLMModel(**model_config, custom_llm_provider='openai')
    agent_factory = PyCallingAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/py_calling_agent_qwen2_5_72b.json")


async def evaluate_qwen2_5_14b():
    # Create a specific agent factory
    model_config = load_model_config("qwen2-5-14b")
    model = LiteLLMModel(**model_config, custom_llm_provider='openai')
    agent_factory = PyCallingAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/py_calling_agent_qwen2_5_14b.json")


async def evaluate_qwen2_5_7b():
    # Create a specific agent factory
    model_config = load_model_config("qwen2-5-7b")
    model = LiteLLMModel(**model_config, custom_llm_provider='openai')
    agent_factory = PyCallingAgentFactory(model)
    await evaluate(agent_factory, ground_truths, "./results/py_calling_agent_qwen2_5_7b.json")

if __name__ == "__main__":
    asyncio.run(evaluate_deepseek_v3())
    # asyncio.run(evaluate_claude3_5_sonnet())
    # asyncio.run(evaluate_gpt_4o())
    # asyncio.run(evaluate_claude3_7_sonnet())
    # asyncio.run(evaluate_qwen3_30b())
    # asyncio.run(evaluate_mistral())