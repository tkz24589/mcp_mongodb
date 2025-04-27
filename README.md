# MongoDB MCP Server

<a href="https://glama.ai/mcp/servers/@mongodb/mcp-mongodb">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@mongodb/mcp-mongodb/badge" alt="MongoDB Server MCP server" />
</a>

## Overview
The MongoDB MCP Server is a **natural language interface** designed for agentic applications to efficiently manage and search data in MongoDB. It integrates seamlessly with **MCP (Model Content Protocol) clients**, enabling AI-driven workflows to interact with structured and unstructured data in MongoDB. Using this MCP Server, you can ask questions like:

- "Store this document in the collection"
- "Create an index on this field"
- "Find documents matching these criteria"
- "Perform an aggregation pipeline"

## Features
- **Natural Language Queries**: Enables AI agents to query and update MongoDB using natural language.
- **Seamless MCP Integration**: Works with any **MCP client** for smooth communication.
- **Full MongoDB Support**: Handles **collections, documents, indexes, and aggregations**.
- **Search & Filtering**: Supports efficient data retrieval and querying in MongoDB.
- **Scalable & Lightweight**: Designed for **high-performance** data operations.

## Tools

This MCP Server provides tools to manage the data stored in MongoDB.

- `collection` tools to create, drop and list collections
- `document` tools to insert, update, delete and query documents
- `index` tools to create and manage indexes for efficient querying
- `aggregation` tools to perform complex data processing pipelines
- `query` tools to find and filter documents with various conditions

## Installation

### Installing via Smithery

To install MongoDB MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@mongodb/mcp-mongodb):

```bash
npx -y @smithery/cli install @mongodb/mcp-mongodb --client claude
```

### Manual Installation
```sh
# Clone the repository
git clone https://github.com/mongodb/mcp-mongodb.git
cd mcp-mongodb

# Install dependencies using uv
uv venv
source .venv/bin/activate
uv sync
```

## Configuration

To configure this MongoDB MCP Server, consider the following environment variables:

| Name                    | Description                                               | Default Value |
|-------------------------|-----------------------------------------------------------|---------------|
| `MONGODB_HOST`          | MongoDB IP or hostname                                    | `"127.0.0.1"` |
| `MONGODB_PORT`          | MongoDB port                                              | `27017`       |
| `MONGODB_USERNAME`      | Database username                                         | None          |
| `MONGODB_PASSWORD`      | Database password                                         | None          |
| `MONGODB_AUTH_SOURCE`   | Authentication database                                   | `"admin"`     |
| `MONGODB_SSL`           | Enables or disables SSL/TLS                               | `False`       |
| `MONGODB_CA_PATH`       | CA certificate for verifying server                       | None          |

## Integration with OpenAI Agents SDK

Integrate this MCP Server with the OpenAI Agents SDK. Read the [documents](https://openai.github.io/openai-agents-python/mcp/) to learn more about the integration of the SDK with MCP.

Install the Python SDK.

```commandline
pip install openai-agents
```

Configure the OpenAI token:

```commandline
export OPENAI_API_KEY="<openai_token>"
```

And run the [application](./examples/mongodb_assistant.py).

```commandline
python3.13 mongodb_assistant.py 
```

You can troubleshoot your agent workflows using the [OpenAI dashboard](https://platform.openai.com/traces/).

## Integration with Claude Desktop
You can configure Claude Desktop to use this MCP Server.

1. Specify your MongoDB credentials and TLS configuration
2. Retrieve your `uv` command full path (e.g. `which uv`)
3. Edit the `claude_desktop_config.json` configuration file 
   - on a MacOS, at `~/Library/Application\ Support/Claude/`

```commandline
{
    "mcpServers": {
        "mongodb": {
            "command": "<full_path_uv_command>",
            "args": [
                "--directory",
                "<your_mcp_server_directory>",
                "run",
                "src/main.py"
            ],
            "env": {
                "MONGODB_HOST": "<your_mongodb_host>",
                "MONGODB_PORT": "<your_mongodb_port>",
                "MONGODB_USERNAME": "<your_mongodb_username>",
                "MONGODB_PASSWORD": "<your_mongodb_password>",
                "MONGODB_AUTH_SOURCE": "<your_auth_source>",
                "MONGODB_SSL": True|False,
                "MONGODB_CA_PATH": "<your_mongodb_ca_path>"
            }
        }
    }
}
```

You can troubleshoot problems by tailing the log file.

```commandline
tail -f ~/Library/Logs/Claude/mcp-server-mongodb.log
```

## Testing

You can use the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) for visual debugging of this MCP Server.

```sh
npx @modelcontextprotocol/inspector uv run src/main.py
```

## Example Use Cases
- **AI Assistants**: Enable LLMs to fetch, store, and process data in MongoDB.
- **Chatbots & Virtual Agents**: Retrieve document data, manage collections, and personalize responses.
- **Data Search & Analytics**: Query MongoDB for **real-time insights and complex aggregations**.
- **Document Processing**: Manage document collections with **flexible schema and indexing**.

## Contributing
1. Fork the repo
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Push to your branch and submit a PR!

## License
This project is licensed under the **MIT License**.

## Contact
For questions or support, reach out via [GitHub Issues](https://github.com/mongodb/mcp-mongodb/issues).
