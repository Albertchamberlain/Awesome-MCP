<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Albertchamberlain/Awesome-MCP/main/assets/logo-dark.svg">
    <img alt="Awesome MCP" src="https://raw.githubusercontent.com/Albertchamberlain/Awesome-MCP/main/assets/logo.svg" width="128">
  </picture>
</p>

<h1 align="center">Awesome MCP</h1>

<p align="center">
  <strong>The MCP catalog your agents can search.</strong>
</p>

<p align="center">
  Curated for humans. Structured in YAML. Searchable through MCP.
</p>

<p align="center">
  <a href="https://github.com/Albertchamberlain/Awesome-MCP"><img alt="Awesome" src="https://cdn.jsdelivr.net/gh/sindresorhus/awesome@main/media/badge.svg"></a>
  <a href="https://pypi.org/project/awesome-mcp/"><img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-4c1?logo=open-source-initiative&logoColor=white"></a>
  <img alt="Catalog" src="https://img.shields.io/badge/catalog-27%20entries-7c3aed">
  <img alt="Updated" src="https://img.shields.io/badge/updated-2026--06--18-059669">
</p>

<br>

<p align="center">
  <a href="#catalog"><b>Catalog</b></a> &ensp;·&ensp;
  <a href="#connect-to-your-agent"><b>Connect an Agent</b></a> &ensp;·&ensp;
  <a href="#cli"><b>CLI</b></a> &ensp;·&ensp;
  <a href="#contributing"><b>Contributing</b></a>
</p>

<br>

---

## The Problem

Most awesome lists are **Markdown walls** — hand-edited, hard to validate, and invisible to AI agents.

They look readable to humans, but every edit risks broken links, inconsistent formatting, and drift between the data and its presentation. And when your agent needs to *discover* the right MCP tool, it has to parse a wall of unstructured text.

## What's Different Here

Awesome MCP keeps the entire MCP ecosystem in **one validated YAML catalog**, then turns it into everything you can see, query, and connect to:

<div align="center">

```
                      catalog.yaml
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                 ▼
      README.md         CLI tools        MCP server
   (human-browsable)  (searchable)   (agent-searchable)
```

</div>

> **Edit one record. Regenerate the docs. Re-query from anywhere.**

- **Humans** browse a clean, categorized list of servers, clients, registries, and SDKs.
- **CLI users** run `awesome-mcp search playwright` and get structured results.
- **AI agents** call `search_catalog` through MCP and discover tools natively.

---

## See It in Action

The meta-server is what makes this project unique. A human or an agent asks a question — and the catalog answers:

```text
User (or Agent):
  "Find an official MCP server for read-only PostgreSQL access."

Agent calls:
  search_catalog({
    "query": "PostgreSQL",
    "kind": "server",
    "limit": 3
  })

Awesome-MCP responds:
  ┌──────────────────────────────────────────────────────────────┐
  │ PostgreSQL Server                              ✅ official   │
  │ Read-only PostgreSQL access with schema introspection.       │
  │ Transport: stdio  ·  Tags: sql, postgres                    │
  └──────────────────────────────────────────────────────────────┘
```

*This is what separates Awesome MCP from every other awesome list. **The catalog speaks MCP.** *

---

## Quick Start

### Connect to Your Agent

Add Awesome MCP to any MCP client so your agent can discover tools:

```bash
# Install globally (recommended)
pipx install awesome-mcp
```

```json
{
  "mcpServers": {
    "awesome-mcp": {
      "command": "awesome-mcp-server"
    }
  }
}
```

Supports **Claude Desktop**, **Cursor**, **Cline**, **Continue**, and any MCP-compatible client.

Once connected, your agent can call these tools:

| Tool | What it does |
|---|---|
| `search_catalog` | Full-text search across names, tags, and descriptions |
| `list_catalog` | List entries filtered by kind (`server`, `client`, …) |
| `get_catalog_entry` | Fetch one entry by stable `id` |
| `catalog_stats` | Summary counts |

### CLI

```bash
# Get an overview
$ awesome-mcp stats

# List every server
$ awesome-mcp list --kind server

# Search for a specific tool
$ awesome-mcp search playwright

  Playwright MCP (playwright-mcp) — server
    Browser automation via Playwright
    Transport: stdio  ·  Tags: browser, automation, microsoft

# Regenerate the catalog sections of this README
$ awesome-mcp readme
```

---

## Catalog

> **27 curated entries** · 13 servers · 6 clients · 4 registries · 4 SDKs/tools · 16 official/reference
> *Deliberately curated — not an exhaustive index.*

Legend: ✅ = Official / reference project · Transport: `stdio`/`sse`/`remote`

<!-- CATALOG:SERVERS:START -->

## 🛠️ MCP Servers

### AI

- [Memory Server](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) ✅ `stdio` — Persistent knowledge-graph memory across conversations. — `memory`, `graph`
- [SandBase CLI](https://github.com/sandbaseai/cli) `stdio` — Local MCP bridge for discovering and running 2,000+ AI models and APIs from 25 supported clients. — `ai`, `models`, `api`, `cli`
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

- [Agentlas OS](https://github.com/agentlas-ai/Agentlas-OS) `stdio` — Local-first agent OS for portable agent and team packages over MCP. — `coding`, `agents`, `runtime`
- [ax](https://github.com/Necmttn/ax) `stdio` — Local-first telemetry and memory graph for AI coding agents. — `coding`, `telemetry`, `local-first`
- [Filesystem Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) ✅ `stdio` — Secure local file read/write with configurable directory allowlists. — `files`, `local`
- [GitHub MCP Server](https://github.com/github/github-mcp-server) ✅ `stdio`, `remote` — Official GitHub integration for repos, issues, PRs, and Actions. — `github`, `git`
- [Official MCP Reference Servers](https://github.com/modelcontextprotocol/servers) ✅ `stdio` — Reference implementations maintained by the MCP steering group (filesystem, memory, fetch, git, and more). — `reference`, `anthropic`

### Marketing

- [NotFair](https://github.com/nowork-studio/NotFair) `stdio` — Open-source Claude Code skills for SEO, GEO, and paid ads — connects to Google Ads MCP, Meta Ads MCP, Google Search Console MCP, and Google Analytics (GA4) MCP for live account data. — `seo`, `google-ads`, `meta-ads`, `marketing`

### Productivity

- [Google Drive Server](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) ✅ `stdio` — List, read, and search files in Google Drive. — `google`, `files`
- [PostEverywhere](https://github.com/posteverywhere/mcp) `stdio`, `remote` — Schedule and publish social posts to 11 platforms with media, campaigns, analytics and AI captions. — `social`, `marketing`

### Social

- [Xquik MCP](https://docs.xquik.com/mcp/overview) `remote` — Remote X data MCP server for search, profiles, timelines, monitoring, webhooks, and confirmation-gated writes. Not affiliated with X Corp. — `x`, `twitter`, `social`, `api`

### Sports

- [Live Tennis API](https://github.com/livetennisapi/livetennisapi-mcp) `stdio` — Real-time tennis match state (score, server, three-valued break-point, retirement/walkover/completed) plus players, rankings, Elo, and fixtures. — `tennis`, `sports`, `real-time`, `data`
- [ParlayAPI](https://github.com/JacobiusMakes/parlay-api-mcp) ✅ `stdio` — Sports odds, player props, public event discovery, and account usage; account data tools use each user's own API key and allowances, with free and paid API tiers. — `sports`, `odds`, `player-props`

### Web

- [Brave Search MCP](https://github.com/brave/brave-search-mcp-server) `stdio` — Web search via Brave Search API. — `search`, `api`
- [BuyWhere MCP](https://github.com/BuyWhere/buywhere-mcp) `remote` — Real-time product search and price comparison across 148M+ products from Singapore, Southeast Asia, and US marketplaces via remote streamable-HTTP. — `search`, `ecommerce`, `api`
- [Fetch Server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) ✅ `stdio` — Fetch and convert web pages to markdown for LLM consumption. — `http`, `scraping`
- [Pocket Drives](https://github.com/RevList/pocket-drives-mcp) `remote` — Search peer-to-peer luxury, exotic, and EV rentals from independent hosts. Booking finishes in the iOS app. Remote streamable HTTP at https://pocketdrives.ai/mcp. — `search`, `travel`, `rental`

<!-- CATALOG:SERVERS:END -->

<!-- CATALOG:CLIENTS:START -->

## 🖥️ MCP Clients

### Desktop

- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) `stdio`, `sse` — Multi-model desktop client with visual MCP server management. — `desktop`, `multi-model`
- [Claude Desktop](https://claude.ai/download) ✅ `stdio` — Anthropic desktop app with native MCP connector support. — `anthropic`, `desktop`

### IDE

- [Cline](https://github.com/cline/cline) `stdio` — VS Code extension agent with MCP server marketplace integration. — `vscode`, `agent`
- [Continue](https://github.com/continuedev/continue) `stdio` — Open-source AI code assistant for VS Code and JetBrains with MCP support. — `vscode`, `open-source`
- [Cursor](https://cursor.com) `stdio`, `sse` — AI-native IDE with first-class MCP server configuration in settings. — `ide`, `coding`

### Web

- [LibreChat](https://github.com/danny-avila/LibreChat) `stdio`, `sse` — Self-hosted ChatGPT-style UI with MCP plugin support. — `self-hosted`, `web`

<!-- CATALOG:CLIENTS:END -->

<!-- CATALOG:REGISTRIES:START -->

## 📚 Registries & Directories

### Directory

- [Glama MCP Directory](https://glama.ai/mcp/servers) `remote` — MCP server directory with quality scores and hosted deployment options. — `directory`, `hosting`
- [MCP Registry (Official)](https://registry.modelcontextprotocol.io) ✅ `remote` — Official MCP server registry and specification hub. — `official`, `spec`
- [MCP.so](https://mcp.so) `remote` — Community-driven searchable directory of MCP servers. — `directory`, `community`
- [MyMCPTools](https://mymcptools.com) `remote` — Directory of MCP servers with scheduled live handshakes — each entry carries an install-time reachability verdict and latency. — `directory`, `uptime`
- [Smithery](https://smithery.ai) `remote` — Curated MCP registry with one-click install flows for popular clients. — `directory`, `install`

<!-- CATALOG:REGISTRIES:END -->

<!-- CATALOG:SDKS:START -->

## 🧰 SDKs & Frameworks

### SDK

- [FastMCP](https://github.com/jlowin/fastmcp) `stdio`, `sse` — High-level Python framework for building MCP servers with decorators. — `python`, `fastapi-style`
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) ✅ `stdio`, `sse` — Official Python SDK for building MCP servers and clients. — `python`, `sdk`
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) ✅ `stdio`, `sse` — Official TypeScript SDK for MCP server and client development. — `typescript`, `sdk`

### Tooling

- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ✅ `stdio` — Visual debugging tool for testing MCP servers during development. — `debug`, `devtools`

<!-- CATALOG:SDKS:END -->

---

## Data Model

Every entry in the catalog is a validated YAML record. No raw Markdown, no drift:

```yaml
- id: postgres-server
  name: PostgreSQL Server
  kind: server
  category: database
  url: https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
  description: Read-only PostgreSQL access with schema introspection.
  transport: [stdio]
  official: true
  tags: [sql, postgres]
```

> **One record. One source of truth.** Every change is validated, and the README is regenerated from it.

---

## Contributing

Add or edit entries in [`data/catalog.yaml`](data/catalog.yaml), then:

```bash
# Validate the catalog
awesome-mcp validate

# Regenerate the README
awesome-mcp readme

# Run the test suite
pytest
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the entry schema, curation policy, and review checklist.

### Curation Philosophy

- **Curated**, not comprehensive — every entry earns its place.
- **Official** projects get the ✅ flag, community projects don't.
- **Stable IDs** mean links never break between catalog updates.
- Entries link to upstream projects under their respective licenses.

---

## Related Lists

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — official reference servers
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — large community list
- [MCP Registry](https://registry.modelcontextprotocol.io) — official MCP registry

---

## Contributors

<a href="https://github.com/Albertchamberlain/Awesome-MCP/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Albertchamberlain/Awesome-MCP" alt="Awesome-MCP contributors" />
</a>

## Star History

<p align="center">
  <img src="https://api.star-history.com/svg?repos=Albertchamberlain/Awesome-MCP&type=Date&sealed_token=1xyCNq0LSU304WvVyoz3q01A6O39ncWD9GT11VJhawLmHIxNsBKw1-YRnoAsuWgMBnRurnBB8omrhm-vRPkstQ8GqaUuUVhDqJaLv17-ct6SOiHHRYi14Q" alt="Star history chart for Albertchamberlain/Awesome-MCP" width="880" />
</p>

---

<br>

<p align="center">
  <sub>MIT — see <a href="LICENSE">LICENSE</a>. Catalog descriptions link to upstream projects under their respective licenses.</sub>
</p>
