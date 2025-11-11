# ==============================================
# Risk Management Tools
# ==============================================
from mcp.server.fastmcp import FastMCP
import random

def register_risk_tools(mcp: FastMCP):
    """Register risk-related tools with the MCP server"""
    
    @mcp.tool()
    def get_customer_risk_score(customer_id: str) -> dict:
        """Calculate risk based on payment delays, claims, and credit"""
        # Mock scoring logic – could later call a GroRiskEngine API
        score = random.uniform(0, 100)
        return {
            "customer_id": customer_id,
            "risk_score": round(score, 2),
            "risk_level": "High" if score < 40 else "Medium" if score < 70 else "Low"
        }
