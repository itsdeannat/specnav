# specnav

A lightweight CLI tool for exploring, describing, and generating example cURL requests from OpenAPI specifications.

## Features

- **Explore**: Get a quick overview of all endpoints in your OpenAPI spec
- **Describe**: View detailed information about specific endpoints, including parameters, request bodies, and responses
- **Generate**: Generate example cURL requests for any endpoint using OpenAPI's GPT-5-mini model

## Installation

Install SpecNav install from source:

```bash
git clone <repository-url>
cd specnav
pip install -e .
```

### Requirements

- Python 3.13+
- `typer>=0.9`
- `pyyaml`
- `openai` (for the generate command)
- `python-dotenv` (for environment configuration)
- `pydantic`

## Quick Start

### Explore an API

View all endpoints and their operations:

```bash
specnav explore oas.json
```

### Describe an endpoint

Get detailed information about a specific endpoint:

```bash
specnav describe oas.json GET /pets
specnav describe oas.json POST /pets
specnav describe oas.json GET /pets/{petId}
```

### Generate example requests

Generate an example cURL request for an endpoint:

```bash
specnav generate oas.json GET /pets
specnav generate oas.json POST /pets
```

## Configuration

To use the `generate` command, you'll need an OpenAI API key. Set it in your environment:

```bash
export OPENAI_API_KEY=your-api-key-here
```

Or create a `.env` file in your project root:

```
OPENAI_API_KEY=your-api-key-here
```

## Project Structure

```
src/
├── internal/           # Core functionality
│   ├── endpoints.py   # Endpoint listing logic
│   ├── llm.py         # LLM integration for request generation
│   └── oas_loader.py  # OpenAPI spec loading
├── schemas/            # Data model
│   └── example_request.py
└── specnav/            # CLI commands
    ├── cli.py         # Main CLI entry point
    ├── explore.py     # Explore command
    ├── describe.py    # Describe command
    └── generate.py    # Generate command
```

## Example OpenAPI spec

The project includes a sample Pet Store API in `oas.json` for testing and demonstration purposes.

## Development

Install development dependencies:

```bash
pipenv install --dev
```

Run the CLI locally:

```bash
python -m specnav.cli explore oas.json
```
