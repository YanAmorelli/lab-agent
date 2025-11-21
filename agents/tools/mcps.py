from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams
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