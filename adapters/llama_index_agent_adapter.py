from typing import List, Callable
import logging
from core.agent import Agent, AgentFactory, AgentResponse, AgentToolCall
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.workflow import Context
from llama_index.core.agent.workflow import ToolCall, AgentOutput

logger = logging.getLogger('Agent.LLamaIndexAgentAdapter')


class LLamaIndexAgentWrapper(Agent):
    """Agent implementation that wraps LlamaIndex's FunctionAgent"""
    
    def __init__(self, model: any, tools: List[Callable] = None):
        """
        Initialize the LLamaIndexAgentWrapper.
        
        Args:
            model: The model to use
            tools: List of callable functions/tools
        """
        
        self._agent = FunctionAgent(tools=tools, llm=model)
        self.ctx = Context(self._agent)
    
    async def _run_with_tracking(self, query: str) -> AgentResponse:
        """
        Run the agent with tracking.
        """
        handler = self._agent.run(query, ctx=self.ctx)
        tool_calls = []
        steps = 0
        async for event in handler.stream_events():
            if type(event) is ToolCall:
                tool_calls.append(AgentToolCall(event.tool_name, event.tool_kwargs, event.tool_id))
            elif type(event) is AgentOutput:
                steps += 1

        return AgentResponse(str(await handler), tool_calls, steps)


    async def run(self, query: str) -> AgentResponse:
        """
        Run the agent with a query and return the response.
        
        Args:
            query: The user input query
            
        Returns:
            The agent's response as an AgentResponse object
        """
            
        return await self._run_with_tracking(query)

class LLamaIndexAgentFactory(AgentFactory):
    """Factory for creating OpenAI agent instances."""
    
    def __init__(self, model: any):
        """
        Initialize the OpenAIAgentFactory.
        
        Args:
            model: The model to use
        """
        self.model = model
    
    def create_agent(self, functions: List[Callable]) -> LLamaIndexAgentWrapper:
        """
        Create an OpenAI agent with the specified functions.
        
        Args:
            functions: List of callable functions
            
        Returns:
            An OpenAIAgentWrapper instance
        """
        return LLamaIndexAgentWrapper(
            model=self.model,
            tools=functions,
        )
