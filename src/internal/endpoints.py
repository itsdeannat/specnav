from rich.table import Table
from rich.console import Console
from rich import box

def list_endpoints(spec: dict):
    """Displays a list of available endpoints, operations, and operation summaries

    Args:
        spec (dict): The OpenAPI specification
    """
    
    paths = spec["paths"]       
    
    print()
    
    for endpoint in paths:
        print(endpoint)
        print_endpoint_table(endpoint, paths)           
                
    
def print_endpoint_table(endpoint: str, paths: str):
    
    available_operations = {'get', 'put', 'post', 'patch', 'delete'} 
    
    table = Table(box=None)
    table.add_column()        
    table.add_column() 
    
    for operation in paths[endpoint]:
        if operation in available_operations:
            operation_details = paths[endpoint][operation]
            try:
                summary = operation_details["summary"]
            except KeyError:
                summary = "✗ Summary missing!"
            table.add_row(f"{operation.upper()}", f"{summary}")
    
    console = Console()
    console.print(table)
    print()
