from typing import List, Callable
import logging
from core.agent import Agent, AgentFactory, AgentResponse, AgentToolCall
from openai.types.responses import ResponseOutputItemAddedEvent, ResponseFunctionToolCall
import json
from agents import Runner
from agents import Agent as OpenAIAgent, function_tool, set_tracing_disabled

set_tracing_disabled(True)

logger = logging.getLogger('Agent.OpenAIAgentAdapter')

class OpenAIAgentWrapper(Agent):
    """Agent implementation that wraps OpenAI's API"""
    
    def __init__(self, model: any, tools: List[Callable] = None):
        """
        Initialize the OpenAIAgent.
        
        Args:
            model: The model to use
            tools: List of callable functions/tools
        """
        self.total_steps = 0
        self.messages = []
        

        self._agent = OpenAIAgent(
            name="AI Agent",
            # instructions=instructions,  
            model=model,
            tools=[function_tool(tool) for tool in tools],
        )
    
    
    async def _run_with_tracking(self, query: str) -> AgentResponse:
        """
        Run the agent with event tracking.
        
        Args:
            query: The user query
            tracker: The OpenAI agent tracker
            
        Returns:
            The agent's response
        """
        self.messages.append({"role": "user", "content": query})
        result = Runner.run_streamed(self._agent, input=self.messages)
        tool_calls = []
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseOutputItemAddedEvent):
                if isinstance(event.data.item, ResponseFunctionToolCall) and event.data.item.type == "function_call":
                    func_name = event.data.item.name
                    

                    # Parse arguments from JSON string
                    try:
                        arguments = json.loads(event.data.item.arguments)
                    except json.JSONDecodeError:
                        # Handle potential invalid JSON
                        arguments = {"_error": "Failed to parse arguments"}
                    
                    tool_call = AgentToolCall(
                        call_id=event.data.item.call_id,
                        function=func_name,
                        arguments=arguments
                    )
                    
                    # Add to call history
                    tool_calls.append(tool_call)

        self.total_steps += result.current_turn
        self.messages += result.to_input_list()

        return AgentResponse(result.final_output, tool_calls)
    
    async def run(self, query: str) -> AgentResponse:
        """
        Run the agent with a query and return the response.
        
        Args:
            query: The user input query
            
        Returns:
            The agent's response as an AgentResponse object
        """
        return await self._run_with_tracking(query)

    def get_total_steps(self) -> int:
        return self.total_steps

class OpenAIAgentFactory(AgentFactory):
    """Factory for creating OpenAI agent instances."""
    
    def __init__(self, model: any):
        """
        Initialize the OpenAIAgentFactory.
        
        Args:
            model_id: The model identifier
            api_key: The API key
            base_url: Optional base URL for the API
        """
        self.model = model
    
    def create_agent(self, functions: List[Callable]) -> OpenAIAgentWrapper:
        """
        Create an OpenAI agent with the specified functions.
        
        Args:
            functions: List of callable functions
            instructions: Optional instructions for the agent
            
        Returns:
            An OpenAIAgentWrapper instance
        """
        return OpenAIAgentWrapper(
            model=self.model,
            tools=functions,
        )


# async def main():
#     # Create a specific agent factory

#     model = OpenAIChatCompletionsModel(
#         model=model_id, 
#         openai_client=AsyncOpenAI(base_url=base_url, api_key=api_key)
#     )
#     agent_factory = OpenAIAgentFactory(
#         model=model
#     )

#     evaluator = AgentEvaluator(agent_factory)

#     # Run evaluation
#     ground_truths = json.load(open("./evaluators/ground_truths.json"))
#     for ground_truth in tqdm(ground_truths, desc="Evaluating scenarios"):
#         scenario_module = importlib.import_module(ground_truth['scenario'])
#         results = await evaluator.evaluate(scenario_module, ground_truth['conversations'])
#         print(results['metrics'])

# if __name__ == "__main__":
#     asyncio.run(main())
