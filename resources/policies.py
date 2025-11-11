# ==============================================
# Policy Resources
# ==============================================
from mcp.server.fastmcp import FastMCP

def register_policy_resources(mcp: FastMCP):
    """Register policy-related resources with the MCP server"""
    
    @mcp.resource("policy://data/security")
    def data_security_policy() -> str:
        """Gro Data & AI Security policy summary"""
        return (
            "All AI calls follow zero-trust principles with field-level encryption and "
            "masking for PII such as PAN, Aadhaar, DL, GST. RAG layers use masked embeddings."
        )
