from typing_extensions import Annotated
import typer
from internal.oas_loader import load_oas_spec
from internal.llm import generate_request

def generate (file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file")], operation: Annotated[str, typer.Argument(help="The operatiion")], path: Annotated[str, typer.Argument(help="Path to inspect")]):
    """Generates and displays an example cURL request.

    Args:
        file (str): The OpenAPI Specification file
        operation (str): The OpenAPI operation (e.g. GET, POST, DELETE)
        path (str): The endpoint (e.g. /photos, /photos/{photoId})
    """
    
    content = load_oas_spec(file)
    response = generate_request(content, operation, path)
    
    curl_command = response.example
    print(curl_command)