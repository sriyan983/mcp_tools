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

# Initialize Enterprise MCP server
mcp = FastMCP("GroEnterpriseMCP")

# ==============================================
# REGISTER ALL TOOLS AND RESOURCES
# ==============================================

# Register business tools
register_trip_tools(mcp)
register_finance_tools(mcp)
register_risk_tools(mcp)

# Register resources
register_policy_resources(mcp)
register_summary_resources(mcp)

# ==============================================
# MAIN EXECUTION
# ==============================================

if __name__ == "__main__":
    mcp.run(transport="stdio")
