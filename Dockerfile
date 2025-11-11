# Start from slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install basic system dependencies and Node (for MCP tooling)
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g mcp-cli && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir fastapi uvicorn mcp fastmcp pydantic

# Expose ports for HTTP & MCP Inspector (optional)
EXPOSE 80
EXPOSE 6274
EXPOSE 6277

# Default command (HTTP mode)
ENV MCP_MODE=http
# CMD ["python", "gro_mcp_server.py"]
CMD ["tail", "-f", "/dev/null"]