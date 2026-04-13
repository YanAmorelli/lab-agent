import os

from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams, StreamableHTTPConnectionParams
from mcp.client.stdio import StdioServerParameters

context7 = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="uvx",
            args=["context7-mcp-python"],            
        ),
        timeout=50
    ),
    errlog=False,
)

github_mcp = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://api.githubcopilot.com/mcp/",
        headers={
            "X-MCP-Toolsets": "default,actions",
            "Authorization": os.getenv("GITHUB_PAT")
        }
    )
)