from typing import List, Callable, Optional
import logging
from core.agent import Agent, AgentFactory, AgentToolCall, AgentResponse
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from langgraph.checkpoint.memory import InMemorySaver
from uuid import uuid4


logger = logging.getLogger('Agent.LangChainAgentWrapper')

class LangChainAgentWrapper(Agent):
    """Agent implementation that wraps OpenAI's API"""
    
    def __init__(self, model_id: str, api_key: str = None, base_url: Optional[str] = None, tools: List[Callable] = None, instructions: Optional[str] = None):
        """
        Initialize the LangChainAgent.
        
        Args:
            model_id: The model identifier
            api_key: The API key
            base_url: Optional base URL for the API
            tools: List of callable functions/tools
            instructions: Optional instructions for the agent
        """
        self.total_steps = 0
        self.session_id = str(uuid4())

        model = ChatAnthropic(
            temperature=0,
            max_tokens=8192,
            model=model_id,
            anthropic_api_key=api_key,
            anthropic_api_url=base_url,
            thinking={"type": "disabled"},
        )

        checkpointer = InMemorySaver()
        self._agent = create_react_agent(
            model=model,
            tools=tools,
            checkpointer=checkpointer
        )
    

    async def _run_with_tracking(self, query: str) -> AgentResponse:
        """
        Run the agent with event tracking.
        
        Args:
            query: The user query
            
        Returns:
            The agent's response
        """

        result = ''
        tool_calls = []

        async for event in self._agent.astream_events({"messages": [("user", query)]}, config={"configurable": {"thread_id": self.session_id}}):
            event_type = event.get("event")
            if event_type == "on_tool_start":
                function_name = event.get('name')
                    
                # Extract arguments from the event data
                arguments = {}
                if 'data' in event and 'input' in event['data']:
                    arguments = event['data']['input']
                
                tool_calls.append(AgentToolCall(
                    call_id=event['run_id'],
                    function=function_name,
                    arguments=arguments
                ))
            elif event_type == "on_chat_model_end":
                event_data = event.get("data", {})
                output = event_data.get("output")

                if not output:
                    continue
                if output.response_metadata.get("finish_reason") == 'stop':
                    result = output.content
                
                self.total_steps += 1

        return AgentResponse(
            tool_calls=tool_calls,
            result=result
        )
    
    async def run(self, query: str) -> AgentResponse:
        """
        Run the agent with a query and return the response.
        
        Args:
            query: The user input query
            
        Returns:
            The agent's response as an AgentResponse object
        """
 
            
        # Run the agent
        return await self._run_with_tracking(query)

    def get_total_steps(self) -> int:
        return self.total_steps

class LangchainAgentFactory(AgentFactory):
    """Factory for creating OpenAI agent instances."""
    
    def __init__(self, model_id: str, api_key: str = None, base_url: Optional[str] = None):
        """
        Initialize the OpenAIAgentFactory.
        
        Args:
            model_id: The model identifier
            api_key: The API key
            base_url: Optional base URL for the API
        """
        self.model_id = model_id
        self.api_key = api_key
        self.base_url = base_url
    
    def create_agent(self, functions: List[Callable], instructions: Optional[str] = None) -> LangChainAgentWrapper:
        """
        Create an OpenAI agent with the specified functions.
        
        Args:
            functions: List of callable functions
            instructions: Optional instructions for the agent
            
        Returns:
            An OpenAIAgentWrapper instance
        """
        return LangChainAgentWrapper(
            model_id=self.model_id,
            api_key=self.api_key,
            base_url=self.base_url,
            tools=functions,
            instructions=instructions
        )
