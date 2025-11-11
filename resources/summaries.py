# ==============================================
# Business Summary Resources
# ==============================================
from mcp.server.fastmcp import FastMCP

def register_summary_resources(mcp: FastMCP):
    """Register summary-related resources with the MCP server"""
    
    @mcp.resource("app://groone/insight")
    def groone_summary() -> str:
        """Summary of GroOne business modules"""
        return (
            "GroOne integrates Freight, Fleet, ServiceMandi, and Finance modules. "
            "Each module exposes APIs for load matching, trip management, payments, and vehicle services. "
            "This resource helps agents understand GroOne's architecture."
        )
