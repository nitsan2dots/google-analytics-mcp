#!/usr/bin/env python
"""FastMCP entry point for Google Analytics MCP server."""

# Import the MCP server object and register all tools
from analytics_mcp.coordinator import mcp

# Import tools to register them (required for the server to work)
from analytics_mcp.tools.admin import info  # noqa: F401
from analytics_mcp.tools.reporting import realtime  # noqa: F401
from analytics_mcp.tools.reporting import core  # noqa: F401

# Expose the server object for FastMCP to find
# FastMCP looks for variables named 'mcp', 'server', or 'app'
server = mcp

if __name__ == "__main__":
    mcp.run()
