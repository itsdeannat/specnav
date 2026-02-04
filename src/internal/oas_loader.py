import json
import yaml
from pathlib import Path

def load_oas_spec (path: str) -> dict:
    """Loads an OpenAPI specification.

    Args:
        path (str): The path to the OAS 

    Returns:
        dict: The parsed OAS content as a dictionary
    """
    
    path = Path(path)
    with open(path, "r", encoding="utf-8") as file:
        if path.suffix == ".json":
                return json.load(file)

        if path.suffix in {".yml", ".yaml"}:
            return yaml.safe_load(file)

        raise ValueError(f"Unsupported OAS file type: {path.suffix}")