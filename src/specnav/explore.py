from typing_extensions import Annotated
import typer
from internal.oas_loader import load_oas_spec
from internal.endpoints import list_endpoints

def explore(file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file")]):
    """Explore all endpoints in an OpenAPI specification.
    
    Displays a summary of all endpoints, including their HTTP methods and brief descriptions. Useful for getting a quick overview of the API.
    
    Example:
        specnav list oas.json

    Args:
        file: Path to the OpenAPI Specification file
    """
    
    content = load_oas_spec(file)
    list_endpoints(content)