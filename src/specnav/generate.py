import os
from typing_extensions import Annotated
from internal.oas_loader import load_oas_spec
from internal.llm import generate_request
import typer

def generate (file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file")], operation: Annotated[str, typer.Argument(help="The operatiion")], path: Annotated[str, typer.Argument(help="Path to inspect")]):
    
    content = load_oas_spec(file)
    response = generate_request(content, operation, path)
    
    curl_command = response.example
    print(curl_command)
    