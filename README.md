# Agent Performance Evaluator

A comprehensive benchmarking framework for evaluating AI agent implementations and their tool-calling capabilities across multiple scenarios.

## Features

- **Multi-Agent Framework Support**: PyCallingAgent, LangChain, LlamaIndex, OpenAI agents
- **Diverse Scenarios**: Weather queries, flight booking, event planning, healthcare data processing, investment analysis, product recommendations
- **Comprehensive Metrics**: Success rates, function call accuracy, argument validation, step efficiency
- **Multi-Model Testing**: GPT-4o, Claude, DeepSeek, Qwen models, and more

## Development

### Adding New Scenarios

1. Create a new scenario file in `scenarios/`
2. Define your functions with proper type hints
3. Add test cases to `ground_truths.json`
4. Update the evaluation pipeline

## Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd agent-performance-evaluator

# Install dependencies using uv
uv sync
```

### Using PyCallingAgent Framework

```python
import asyncio
from adapters.py_calling_agent_adapter import PyCallingAgentFactory
from py_calling_agent.models import LiteLLMModel
from evaluation import evaluate
import json

# Load test scenarios
ground_truths = json.load(open("./scenarios/ground_truths.json"))

# Create agent factory
model = LiteLLMModel(
    model_id="gpt-4o",
    api_key="your-api-key",
    base_url="your-base-url",
    custom_llm_provider='openai'
)
agent_factory = PyCallingAgentFactory(model)

# Run evaluation
async def main():
    await evaluate(agent_factory, ground_truths, "./results/results.json")

asyncio.run(main())
```

### Using Other ToolCalling Agent Frameworks

```python
# LangChain Agent
from adapters.langchain_agent_adapter import LangChainAgentFactory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")
agent_factory = LangChainAgentFactory(llm)
await evaluate(agent_factory, ground_truths, "./results/langchain_results.json")

# LlamaIndex Agent
from adapters.llama_index_agent_adapter import LLamaIndexAgentFactory
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-4o")
agent_factory = LLamaIndexAgentFactory(llm)
await evaluate(agent_factory, ground_truths, "./results/llama_index_results.json")
```

## Project Structure

```
├── adapters/                 # Agent implementation adapters
│   ├── py_calling_agent_adapter.py
│   ├── langchain_agent_adapter.py
│   ├── llama_index_agent_adapter.py
│   └── openai_agent_adapter.py
├── core/                     # Core evaluation logic
│   ├── evaluator.py         # Main evaluation engine
│   ├── agent.py             # Agent interface definitions
│   └── validation.py        # Function call validation
├── scenarios/               # Test scenarios and ground truths
│   ├── weather_query.py
│   ├── flight_booking.py
│   ├── event_planning.py
│   └── ground_truths.json
├── results/                 # Evaluation results
└── evaluation.py           # Main evaluation runner
```

## Evaluation Metrics

- **Success Rate**: Percentage of successful turns
- **Function Call Accuracy**: Missing calls, wrong arguments, type mismatches
- **Step Efficiency**: Number of steps per conversation
- **Argument Validation**: Missing, wrong type, or incorrect values

