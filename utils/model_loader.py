import tomllib
from typing import TypedDict

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