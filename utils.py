import tomllib
from typing import TypedDict, Callable
import inspect

class ModelConfig(TypedDict):
    model_id: str
    api_key: str
    base_url: str

def load_model_config(model_name: str) -> ModelConfig:
    """Load model configuration from models.toml"""
    with open("models.toml", "rb") as f:
        models = tomllib.load(f)
    
    if model_name not in models:
        available = list(models.keys())
        raise ValueError(f"Model '{model_name}' not found. Available: {available}")
    
    return models[model_name]


def function_to_schema(func: Callable) -> dict:
    """
    Convert a Python function to an OpenAI tool schema.
    """
    type_map = {
        str: "string",
        int: "integer", 
        float: "number",
        bool: "boolean",
        list: "array",
        dict: "object",
        type(None): "null",
    }

    try:
        signature = inspect.signature(func)
    except ValueError as e:
        raise ValueError(
            f"Failed to get signature for function {func.__name__}: {str(e)}"
        )

    parameters = {}
    for param in signature.parameters.values():
        try:
            param_type = type_map.get(param.annotation, "string")
        except KeyError:
            param_type = "string"
        parameters[param.name] = {"type": param_type}

    required = [
        param.name
        for param in signature.parameters.values()
        if param.default == inspect._empty
    ]

    return {
            "name": func.__name__,
            "description": func.__doc__ or "",
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": required,
            }
        }