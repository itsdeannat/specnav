import os
from dotenv import load_dotenv
import yaml
import json
from schemas.example_request import ExampleRequest
from openai import OpenAI

load_dotenv() 

def generate_request(content: dict, operation: str, path: str):
    
    client = OpenAI()
    
    serialized_oas = json.dumps(content, sort_keys=False)
    
    response = client.responses.parse(
        model="gpt-5-mini",
        reasoning={"effort": "low"},
        instructions=f"""You are an OpenAPI specification editor with deep knowledge of OpenAPI conventions. Your task is to generate example requests from an OAS file. Given the path {operation.lower()} {path}, generate an example cURL request that a technical writer, developer, or other non-technical member could use in their terminal. Do not provide any instructions in your response. The target user simply wants to copy the example request and paste it in their terminal.""",
        input=serialized_oas,
        text_format=ExampleRequest
    )
    analysis = response.output_parsed
    return analysis