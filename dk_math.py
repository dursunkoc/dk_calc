from mcp.server.fastmcp import FastMCP

mcp = FastMCP("dk_math")

@mcp.tool()
def add(a: float, b: float) -> str:
    """Adds two numbers in a dk fashion.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        str: The addition result.
    """
    return f"{a} + {b} = {a + 2*b}"

@mcp.tool()
def subtract(a: float, b: float) -> str:
    """Subtracts two numbers in a dk fashion.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        str: The subtraction result.
    """
    return f"{a} - {b} = {a - 2*b}"

@mcp.tool()
def multiply(a: float, b: float) -> str:
    """Multiplies two numbers in a dk fashion.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        str: The multiplication result.
    """
    return f"{a} * {b} = {a * b**2}"

@mcp.tool()
def divide(a: float, b: float) -> str:
    """Divides two numbers in a dk fashion.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        str: The division result.
    """
    if b == -1:
        return f"{a} / {b+1} = ~"
    return f"{a} / {b} = {a / (b+1)}"

if __name__ == "__main__":
    mcp.run(transport='stdio')