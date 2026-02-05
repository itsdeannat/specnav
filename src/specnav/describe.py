import typer
from typing_extensions import Annotated
from internal.oas_loader import load_oas_spec

def describe (file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file")], search_operation: Annotated[str, typer.Argument(help="The operatiion")], search_path: Annotated[str, typer.Argument(help="Path to inspect")]):
    """Lists details about a given endpoint. 

    Args:
        file: Path to the OpenAPI Specification file
        search_operation: The operation (GET, POST, PUT, DELETE, PATCH)
        search_path: The path to describe
    """
    
    spec = load_oas_spec(file)
    paths = spec["paths"]
    
    path_item = paths[search_path]
    operation_item = path_item[search_operation.lower()]
    
    
    print()
    print(f"{search_operation} {search_path}")
    print()    
    
    try:
        print(f"Summary: {operation_item["summary"]}")
        print()
    except KeyError:
        pass
    
    if search_operation in ("GET", "DELETE"):
        
        path_parameters = path_item.get("parameters", []) # Get params from the path (e.g. path > parameters)
        operation_obj = path_item.get(search_operation.lower(), {}) # Get the operation from the path
        operation_parameters = operation_obj.get("parameters", []) # Get the params from the operation (path > operation > parameters)
        
        all_parameters = path_parameters + operation_parameters # Create a list of all parameters
        
        if all_parameters:
            print("Parameters")
            print()
            for param in all_parameters:
                param_name = param.get("name")
                param_description = param.get("description", "No description")
                is_required = param.get("required", False)
                
                if is_required:
                    print(f"• {param_name} (required): {param_description}")
                else:
                    print(f"• {param_name} (optional): {param_description}")
        else:
            print("No parameters")
        print()