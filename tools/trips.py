# ==============================================
# Trip Management Tools
# ==============================================
from mcp.server.fastmcp import FastMCP
from datetime import datetime
import random

def register_trip_tools(mcp: FastMCP):
    """Register trip-related tools with the MCP server"""
    
    @mcp.tool()
    def get_trip_insights(customer_id: str) -> dict:
        """Fetch summary metrics for all trips related to a customer"""
        # Mocked – in real case, fetch from PostgreSQL/BigQuery
        return {
            "customer_id": customer_id,
            "total_trips": 128,
            "on_time_delivery": "94%",
            "average_tonnage": "22.5 MT",
            "carbon_emission_tCO2e": 19.4,
            "last_updated": datetime.now().isoformat()
        }

    @mcp.tool()
    def get_active_vehicles(zone: str) -> dict:
        """Return fleet summary for active vehicles in a zone"""
        return {
            "zone": zone,
            "total_active": random.randint(80, 150),
            "under_maintenance": random.randint(3, 10),
            "idle": random.randint(5, 15),
            "last_sync": datetime.now().isoformat()
        }

    @mcp.tool()
    def recommend_best_route(source: str, destination: str) -> dict:
        """AI-based recommendation for optimal route"""
        # Later this can call your RAG / ML route optimizer
        return {
            "source": source,
            "destination": destination,
            "recommended_route": f"{source} → Salem → Hosur → {destination}",
            "distance_km": 341,
            "estimated_cost": 21450,
            "fuel_saving_percent": 7.3
        }
