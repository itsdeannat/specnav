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
        
    if search_operation == "POST":
        request_body = operation_item.get("requestBody")
        
        if request_body:
            is_required = request_body.get("required", False)
            
            if is_required:                
                print("Request Body (required): ")
            else: 
                print("Request Body (optional): ")
                
        content = request_body.get("content", {})
        for content_type, content_data in content.items():
            print(f"  Content-Type: {content_type}")
            print()
            
        schema_data = content_data.get("schema")
        
        if "$ref" in schema_data:
                ref = schema_data["$ref"]
                schema_name = ref.split("/")[-1]
                schema = spec.get("components", {}).get("schemas", {}).get(schema_name, {})
        else:
            schema = schema_data
    
        properties = schema.get("properties", {})
        required_fields = schema.get("required", [])
        
        if properties:
            print("Properties")
            for prop_name, prop_data in properties.items():
                prop_type = prop_data.get("type", "unknown")
                prop_description = prop_data.get("description", "No description")
                
                if prop_name in required_fields:
                    print(f" • {prop_name} ({prop_type} required): {prop_description}")
                else:
                    print(f" • {prop_name} ({prop_type} optional): {prop_description}")
    print()
    print("Responses")
    inspect_responses = operation_item.get("responses")
    for response, response_data in inspect_responses.items():
        status_description = response_data.get("description")
        print(f" {response} - {status_description}")