# ==============================================
# Finance Management Tools
# ==============================================
from mcp.server.fastmcp import FastMCP

def register_finance_tools(mcp: FastMCP):
    """Register finance-related tools with the MCP server"""
    
    @mcp.tool()
    def get_pending_invoices(app_id: str, month: str) -> list:
        """Return pending invoices for an application and month"""
        # Would query finance microservice DB
        return [
            {"invoice_id": "INV1023", "amount": 45000, "status": "Pending"},
            {"invoice_id": "INV1089", "amount": 78000, "status": "Pending"}
        ]
