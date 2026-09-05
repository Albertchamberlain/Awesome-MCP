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
  <img alt="Catalog" src="https://img.shields.io/badge/catalog-38%20entries-7c3aed">
  <img alt="Updated" src="https://img.shields.io/badge/updated-2026--09--05-059669">
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

<!-- CATALOG:SERVERS:END -->

<!-- CATALOG:CLIENTS:START -->

<!-- CATALOG:CLIENTS:END -->

<!-- CATALOG:REGISTRIES:START -->

<!-- CATALOG:REGISTRIES:END -->

<!-- CATALOG:SDKS:START -->

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
