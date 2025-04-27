import sys

from common.connection import MongoDBConnectionManager
from common.server import mcp
import tools.document
import tools.collection
import tools.index
import tools.aggregation
from common.config import MCP_TRANSPORT


class MongoDBMCPServer:
    def __init__(self):
        print("Starting the MongoDBMCPServer", file=sys.stderr)

    def run(self):
        mcp.run(transport=MCP_TRANSPORT)

if __name__ == "__main__":
    server = MongoDBMCPServer()
    server.run()
