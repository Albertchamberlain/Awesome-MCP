# Awesome-MCP

![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@main/media/badge.svg)

A **maintainable** curated list of Model Context Protocol (MCP) servers, clients, registries, and SDKs.

Unlike a hand-edited markdown wall, this repo stores entries in [`data/catalog.yaml`](data/catalog.yaml) and ships tooling to **search**, **validate**, and **serve** the catalog as an MCP meta-server.

- **28** curated entries
- **14** servers · **6** clients · **4** registries · **4** SDKs/tools
- **16** official / reference projects
- Catalog updated: `2026-06-18`

## Quick Start

```bash
git clone https://github.com/Albertchamberlain/Awesome-MCP.git
cd Awesome-MCP
pip install -e .

# CLI
awesome-mcp stats
awesome-mcp list --kind server
awesome-mcp search playwright

# Regenerate README from catalog.yaml
awesome-mcp readme

# Run the meta MCP server (search this catalog from any MCP client)
awesome-mcp-server
```

## MCP Meta-Server

This repo includes a small MCP server that exposes the catalog to agents:

| Tool | Description |
|------|-------------|
| `search_catalog` | Full-text search across names, tags, and descriptions |
| `list_catalog` | List entries filtered by kind (`server`, `client`, …) |
| `get_catalog_entry` | Fetch one entry by stable `id` |
| `catalog_stats` | Summary counts |

**Cursor / Claude Desktop config example:**

```json
{
  "mcpServers": {
    "awesome-mcp": {
      "command": "awesome-mcp-server",
      "args": []
    }
  }
}
```

## Contents

## 🛠️ MCP Servers

### Ai

- [Memory Server](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) ✅ `stdio` — Persistent knowledge-graph memory across conversations. — `memory`, `graph`
- [Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) ✅ `stdio` — Structured step-by-step reasoning tool for complex problems. — `reasoning`, `planning`

### Browser

- [Playwright MCP](https://github.com/microsoft/playwright-mcp) `stdio` — Browser automation via Playwright — navigate, click, screenshot, extract content. — `browser`, `automation`, `microsoft`
- [Puppeteer Server](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) ✅ `stdio` — Headless Chrome automation for scraping and interaction. — `browser`, `chrome`

### Communication

- [Slack Server](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) ✅ `stdio` — Post messages and read channels in Slack workspaces. — `slack`, `chat`

### Database

- [PostgreSQL Server](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) ✅ `stdio` — Read-only PostgreSQL access with schema introspection. — `sql`, `postgres`
- [SQLite Server](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) ✅ `stdio` — Query and inspect SQLite databases with schema discovery. — `sql`, `database`

### Developer Tools

- [ax](https://github.com/Necmttn/ax) `stdio` — Local-first telemetry and memory graph for AI coding agents. — `coding`, `telemetry`, `local-first`
- [Filesystem Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) ✅ `stdio` — Secure local file read/write with configurable directory allowlists. — `files`, `local`
- [GitHub MCP Server](https://github.com/github/github-mcp-server) ✅ `stdio, remote` — Official GitHub integration for repos, issues, PRs, and Actions. — `github`, `git`
- [Official MCP Reference Servers](https://github.com/modelcontextprotocol/servers) ✅ `stdio` — Reference implementations maintained by the MCP steering group (filesystem, memory, fetch, git, and more). — `reference`, `anthropic`

### Productivity

- [Google Drive Server](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) ✅ `stdio` — List, read, and search files in Google Drive. — `google`, `files`

### Web

- [Brave Search MCP](https://github.com/brave/brave-search-mcp-server) `stdio` — Web search via Brave Search API. — `search`, `api`
- [Fetch Server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) ✅ `stdio` — Fetch and convert web pages to markdown for LLM consumption. — `http`, `scraping`

## 🖥️ MCP Clients

### Desktop

- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) `stdio, sse` — Multi-model desktop client with visual MCP server management. — `desktop`, `multi-model`
- [Claude Desktop](https://claude.ai/download) ✅ `stdio` — Anthropic desktop app with native MCP connector support. — `anthropic`, `desktop`

### Ide

- [Cline](https://github.com/cline/cline) `stdio` — VS Code extension agent with MCP server marketplace integration. — `vscode`, `agent`
- [Continue](https://github.com/continuedev/continue) `stdio` — Open-source AI code assistant for VS Code and JetBrains with MCP support. — `vscode`, `open-source`
- [Cursor](https://cursor.com) `stdio, sse` — AI-native IDE with first-class MCP server configuration in settings. — `ide`, `coding`

### Web

- [LibreChat](https://github.com/danny-avila/LibreChat) `stdio, sse` — Self-hosted ChatGPT-style UI with MCP plugin support. — `self-hosted`, `web`

## 📚 Registries & Directories

### Directory

- [Glama MCP Directory](https://glama.ai/mcp/servers) `remote` — MCP server directory with quality scores and hosted deployment options. — `directory`, `hosting`
- [MCP Registry (Official)](https://registry.modelcontextprotocol.io) ✅ `remote` — Official MCP server registry and specification hub. — `official`, `spec`
- [MCP.so](https://mcp.so) `remote` — Community-driven searchable directory of MCP servers. — `directory`, `community`
- [Smithery](https://smithery.ai) `remote` — Curated MCP registry with one-click install flows for popular clients. — `directory`, `install`

## 🧰 SDKs & Frameworks

### Sdk

- [FastMCP](https://github.com/jlowin/fastmcp) `stdio, sse` — High-level Python framework for building MCP servers with decorators. — `python`, `fastapi-style`
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) ✅ `stdio, sse` — Official Python SDK for building MCP servers and clients. — `python`, `sdk`
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) ✅ `stdio, sse` — Official TypeScript SDK for MCP server and client development. — `typescript`, `sdk`

### Tooling

- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ✅ `stdio` — Visual debugging tool for testing MCP servers during development. — `debug`, `devtools`

## Contributing

Add or edit entries in [`data/catalog.yaml`](data/catalog.yaml), then run:

```bash
awesome-mcp readme
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry schema and review checklist.

## Related Lists

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — official reference servers
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — large community list
- [MCP Registry](https://registry.modelcontextprotocol.io) — official registry

## License

MIT — see [LICENSE](LICENSE). Catalog descriptions link to upstream projects under their respective licenses.
