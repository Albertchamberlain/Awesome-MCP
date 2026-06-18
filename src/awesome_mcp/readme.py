"""Generate README.md from the YAML catalog."""

from __future__ import annotations

from pathlib import Path

from .catalog import Catalog, Kind, load_catalog

KIND_ORDER: tuple[Kind, ...] = ("server", "client", "registry", "framework")
KIND_EMOJI = {
    "server": "🛠️",
    "client": "🖥️",
    "registry": "📚",
    "framework": "🧰",
}


def _format_entry(entry) -> str:
    official = " ✅" if entry.official else ""
    transport = f" `{', '.join(entry.transport)}`" if entry.transport else ""
    tags = ", ".join(f"`{tag}`" for tag in entry.tags[:4])
    tag_line = f" — {tags}" if tags else ""
    return (
        f"- [{entry.name}]({entry.url}){official}{transport} — "
        f"{entry.description}{tag_line}"
    )


def _section_for_kind(catalog: Catalog, kind: Kind) -> str:
    label = catalog.categories.get(kind, {}).get("label", kind.title())
    emoji = KIND_EMOJI.get(kind, "")
    lines = [f"## {emoji} {label}", ""]
    entries = catalog.by_kind(kind)
    if not entries:
        lines.append("_No entries yet._")
        lines.append("")
        return "\n".join(lines)

    grouped: dict[str, list] = {}
    for entry in entries:
        grouped.setdefault(entry.category, []).append(entry)

    for category in sorted(grouped):
        lines.append(f"### {category.replace('-', ' ').title()}")
        lines.append("")
        for entry in sorted(grouped[category], key=lambda item: item.name.lower()):
            lines.append(_format_entry(entry))
        lines.append("")
    return "\n".join(lines)


def render_readme(catalog: Catalog) -> str:
    stats = catalog.stats()
    body = [
        "# Awesome-MCP",
        "",
        "![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@main/media/badge.svg)",
        "",
        "A **maintainable** curated list of Model Context Protocol (MCP) servers, clients, registries, and SDKs.",
        "",
        "Unlike a hand-edited markdown wall, this repo stores entries in [`data/catalog.yaml`](data/catalog.yaml) "
        "and ships tooling to **search**, **validate**, and **serve** the catalog as an MCP meta-server.",
        "",
        f"- **{stats['total']}** curated entries",
        f"- **{stats.get('server', 0)}** servers · **{stats.get('client', 0)}** clients · "
        f"**{stats.get('registry', 0)}** registries · **{stats.get('framework', 0)}** SDKs/tools",
        f"- **{stats.get('official', 0)}** official / reference projects",
        f"- Catalog updated: `{catalog.meta.updated}`",
        "",
        "## Quick Start",
        "",
        "```bash",
        "git clone https://github.com/Albertchamberlain/Awesome-MCP.git",
        "cd Awesome-MCP",
        "pip install -e .",
        "",
        "# CLI",
        "awesome-mcp stats",
        "awesome-mcp list --kind server",
        "awesome-mcp search playwright",
        "",
        "# Regenerate README from catalog.yaml",
        "awesome-mcp readme",
        "",
        "# Run the meta MCP server (search this catalog from any MCP client)",
        "awesome-mcp-server",
        "```",
        "",
        "## MCP Meta-Server",
        "",
        "This repo includes a small MCP server that exposes the catalog to agents:",
        "",
        "| Tool | Description |",
        "|------|-------------|",
        "| `search_catalog` | Full-text search across names, tags, and descriptions |",
        "| `list_catalog` | List entries filtered by kind (`server`, `client`, …) |",
        "| `get_catalog_entry` | Fetch one entry by stable `id` |",
        "| `catalog_stats` | Summary counts |",
        "",
        "**Cursor / Claude Desktop config example:**",
        "",
        "```json",
        "{",
        '  "mcpServers": {',
        '    "awesome-mcp": {',
        '      "command": "awesome-mcp-server",',
        '      "args": []',
        "    }",
        "  }",
        "}",
        "```",
        "",
        "## Contents",
        "",
    ]

    for kind in KIND_ORDER:
        body.append(_section_for_kind(catalog, kind))

    body.extend(
        [
            "## Contributing",
            "",
            "Add or edit entries in [`data/catalog.yaml`](data/catalog.yaml), then run:",
            "",
            "```bash",
            "awesome-mcp readme",
            "pytest",
            "```",
            "",
            "See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry schema and review checklist.",
            "",
            "## Related Lists",
            "",
            "- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — official reference servers",
            "- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — large community list",
            "- [MCP Registry](https://registry.modelcontextprotocol.io) — official registry",
            "",
            "## License",
            "",
            "MIT — see [LICENSE](LICENSE). Catalog descriptions link to upstream projects under their respective licenses.",
            "",
        ]
    )
    return "\n".join(body)


def write_readme(path: Path | None = None, catalog: Catalog | None = None) -> Path:
    resolved_catalog = catalog or load_catalog()
    readme_path = path or Path(__file__).resolve().parents[2] / "README.md"
    readme_path.write_text(render_readme(resolved_catalog), encoding="utf-8", newline="\n")
    return readme_path
