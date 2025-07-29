from typing import List, Callable
from core.evaluator import Agent, AgentFactory
from adapters.py_calling_agent_tracker import PyCallingAgentTracker
from py_calling_agent import PyCallingAgent, LogLevel, Model
from py_calling_agent.python_runtime import PythonRuntime, Function
from core.agent import AgentResponse
import logging

logger = logging.getLogger('Agent.PyCallingAgentAdapter')


AGENT_IDENTITY = """
You are a tool-augmented agent specializing in Python programming that enables function-calling through LLM code generation and provides runtime state management. 
You have to leverage your inherent Python coding capabilities to interact with tools through a Python runtime environment, allowing direct access to execution results and runtime state.
The user will give you a task and you should solve it by writing Python code in the Python environment provided.
Write comprehensive code solutions that solve the user's request completely in a single execution whenever possible. Avoid unnecessary step-by-step iterations.
"""
class PyCallingAgentWrapper(Agent):
    """Agent implementation that wraps PyCallingAgent"""
    
    def __init__(self, model: Model, functions: List[Callable] = None):
        """
        Initialize the PyCallingAgentWrapper.
        
        Args:
            model: The model to use
            functions: List of callable functions
        """
        functions = [Function(f) for f in functions]

        runtime = PythonRuntime(
            functions=functions,
        )


        self._agent = PyCallingAgent(model=model, runtime=runtime, max_steps=1, max_history=200, log_level=LogLevel.INFO, agent_identity=AGENT_IDENTITY)
        self._functions = [f.name for f in functions]
        self._previous_steps = 0

    
    async def run(self, query: str) -> AgentResponse:
        """
        Run the agent with a query and return the response.
        
        Args:
            query: The user input query
            
        Returns:
            The agent's response as an AgentResponse object
        """
        tracker = PyCallingAgentTracker(target_functions=self._functions)
        # Start tracking
        tracker.start()
        
        # Run the agent
        result = await self._agent.run(query)
        
        # Stop tracking
        tracker.stop()

        total_steps = result.steps_taken

        current_steps = total_steps - self._previous_steps

        self._previous_steps = current_steps
        
        return AgentResponse(result.content, tracker.get_tool_calls(), current_steps)


class PyCallingAgentFactory(AgentFactory):
    """Factory for creating PyCallingAgent instances."""
    
    def __init__(self, model: Model):
        """
        Initialize the PyCallingAgentFactory.
        
        Args:
            model_id: The model identifier
        """
        self.model = model
    
    def create_agent(self, functions: List[Callable]) -> PyCallingAgentWrapper:
        """
        Create a PyCallingAgent with the specified functions.
        
        Args:
            functions: List of callable functions
        Returns:
            A PyCallingAgentWrapper instance
        """
        return PyCallingAgentWrapper(
            model=self.model,
            functions=functions
        )

