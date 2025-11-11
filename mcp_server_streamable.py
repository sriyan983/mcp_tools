# ==============================================
# Gro Enterprise MCP Server - Main Entrypoint
# ==============================================
from mcp.server.fastmcp import FastMCP

# Import tool and resource modules
from tools.trips import register_trip_tools
from tools.finance import register_finance_tools
from tools.risk import register_risk_tools
from resources.policies import register_policy_resources
from resources.summaries import register_summary_resources
import os

import dotenv
dotenv.load_dotenv()

def register_tools_and_resources(mcp):  
    # Register business tools
    register_trip_tools(mcp)
    register_finance_tools(mcp)
    register_risk_tools(mcp)

    # Register resources
    register_policy_resources(mcp)
    register_summary_resources(mcp)

mcp = FastMCP("GroEnterpriseMCP")
register_tools_and_resources(mcp)

if __name__ == "__main__":
    print("Starting MCP server as streamable mode")
    
    # For HTTP mode, create a new instance with host/port config
    mcp_http = FastMCP(
        name="GroEnterpriseMCP",
        host="0.0.0.0",        # ← Set here
        port=6060,             # ← Set here
    # ... other config options
    )
    register_tools_and_resources(mcp_http)
    mcp_http.run(transport="streamable-http")
