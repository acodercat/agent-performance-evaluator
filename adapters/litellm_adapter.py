from typing import List, Callable
import json
import logging
from core.agent import Agent, AgentFactory, AgentResponse, AgentToolCall
from litellm import acompletion
from utils import function_to_schema

logger = logging.getLogger('Agent.LitellmAdapter')

class LitellmModel:
    """Model implementation that wraps Litellm's model"""

    def __init__(self, model_id: str, api_key: str, base_url: str, provider: str):
        """
        Initialize the LitellmModel.
        """
        self.model_id = model_id
        self.api_key = api_key
        self.base_url = base_url
        self.provider = provider


class LitellmAgentWrapper(Agent):
    """Agent implementation that wraps Litellm's FunctionAgent"""
    
    def __init__(self, model: LitellmModel, tools: List[Callable] = []):
        """
        Initialize the LitellmAgentWrapper.
        
        Args:
            model: The model to use
            tools: List of callable functions/tools
        """
     
        self._model = model
        
        self._tools = [{"type": "function", "function": function_to_schema(tool)} for tool in tools]
        # print(function_to_schema(tools[0]))
     

    async def _run_with_tracking(self, query: str) -> AgentResponse:
        """
        Run the agent with tracking.
        """
        response = await acompletion(
            model=self._model.model_id,
            api_key=self._model.api_key,
            base_url=self._model.base_url,
            custom_llm_provider=self._model.provider,
            tools=self._tools,
            parallel_tool_calls=True,
            tool_choice="auto",
            messages=[{"role": "user", "content": query}],
        )

        tool_calls = []
        # print(f"Response: {response.choices}")
        for choice in response.choices:
            if choice.finish_reason == "tool_calls":
                for item in choice.message.tool_calls:
                    tool_call = AgentToolCall(
                        call_id=item.id,
                        function=item.function.name,
                        arguments=json.loads(item.function.arguments)
                    )
                    tool_calls.append(tool_call)

        return AgentResponse(str(response.choices[0].message.content), tool_calls, 1)


    async def run(self, query: str) -> AgentResponse:
        """
        Run the agent with a query and return the response.
        
        Args:
            query: The user input query
            
        Returns:
            The agent's response as an AgentResponse object
        """
        # print(f"Running LitellmAgentWrapper with query: {query}")
            
        return await self._run_with_tracking(query)
    

class LitellmAgentFactory(AgentFactory):
    """Factory for creating OpenAI agent instances."""
    
    def __init__(self, model: LitellmModel):
        """
        Initialize the OpenAIAgentFactory.
        
        Args:
            model: The model to use
        """
        self.model = model
    
    def create_agent(self, functions: List[Callable]) -> LitellmAgentWrapper:
        """
        Create an OpenAI agent with the specified functions.
        
        Args:
            functions: List of callable functions
            
        Returns:
            An OpenAIAgentWrapper instance
        """
    
        return LitellmAgentWrapper(
            model=self.model,
            tools=functions,
        )
