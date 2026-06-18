# Contributing to Awesome-MCP

Thanks for helping grow the catalog.

## Adding an entry

1. Edit [`data/catalog.yaml`](data/catalog.yaml)
2. Run validation and regenerate docs:

```bash
pip install -e ".[dev]"
awesome-mcp validate
awesome-mcp readme
pytest
```

3. Open a PR with a short note on why the project belongs in the list

## Entry schema

```yaml
- id: unique-kebab-case-id
  name: Human-readable name
  kind: server          # server | client | registry | framework
  category: browser     # free-form grouping within the kind
  url: https://github.com/org/project
  description: One sentence on what it does for MCP users.
  transport: [stdio]    # optional: stdio, sse, remote
  official: false       # true for MCP steering-group / vendor official projects
  tags: [browser, automation]
```

## Review checklist

- Link resolves and points to the canonical repo or product page
- Description is accurate and not marketing fluff
- Prefer actively maintained projects with clear MCP support
- Avoid duplicate entries — search the catalog first: `awesome-mcp search <name>`
- Do not submit paid/spam listings

## MCP meta-server

The catalog is also exposed as an MCP server (`awesome-mcp-server`) so agents can discover resources programmatically. If you add fields to the YAML schema, update:

- `src/awesome_mcp/catalog.py`
- `src/awesome_mcp/server.py`
- tests in `tests/`

## License

By contributing, you agree your commits are licensed under the repository MIT license.
