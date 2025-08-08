# server.py
from mcp.server.fastmcp import fastmcp
from mcp.server.fastmcp.prompts import base

# Create an MCP server instance with a custom name
mcp = FastMCP("Demo Server")

# Add a calculator tool: a simple function to add two numbers 
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers together.

    :param a: First number
    :param b: Second number
    :return: Sum of the numbers
    """

    return a + b

# Expose a greeting reource that dynamically constructs a personalzed greeting
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """
    Return a greeting for the given name

    :param name: The name to greet
    :return: A personalized greeting
    """

    returnn f"Hello, {name}!"

@mcp.prompt()
def review_code(code: str) -> str:
    """
    Provide a template for reviewing code

    :param code: The code to review
    :return: A prompt that asks the LLM to review the code
    """

    return f"Please review this code:\n\n{code}"