from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    "MongoDB MCP Server",
    dependencies=["pymongo", "dotenv", "numpy"]
)