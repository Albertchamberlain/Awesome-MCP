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

## Quick review notes

- Link resolves and points to the canonical repo or product page
- Description is accurate and not marketing fluff
- Prefer actively maintained projects with clear MCP support
- Avoid duplicate entries — search the catalog first: `awesome-mcp search <name>`
- Do not submit paid/spam listings; disclose pricing in the PR template instead



## Security and pricing disclosures

Every catalog PR must fill the pull-request template sections on authentication, data egress, read/write/destructive operations, confirmation boundaries, source/license, and pricing or free-tier limits. Maintainers use these answers during review; omitting them delays merge.

### `official: true` is not a security review

Set `official: true` only for MCP steering-group or vendor-official projects. That flag does **not** mean:

- the entry passed a security audit,
- the project is open source, or
- Awesome-MCP or any steering group endorses its safety or pricing.

### Examples

**Safe read-only.** A local stdio server that lists files under a user-chosen directory, makes no network calls, is MIT-licensed, and has no paid API. The PR body can be short: authentication = none, egress = none, operations = read-only, confirmation = not applicable, source = MIT link, pricing = free forever.

**Hosted write-capable.** A remote MCP that creates tickets in a SaaS product with an API key. Call out that ticket text leaves the machine, that create/update are writes, which actions need confirmation, the license or proprietary status, and free-tier or paid limits.

## Review checklist

Before opening the PR:

- [ ] PR template security and commercial fields are complete
- [ ] `awesome-mcp validate` and `awesome-mcp readme` were run
- [ ] `pytest` passes
- [ ] Link resolves; description is accurate; no duplicate of an existing entry

## MCP meta-server

The catalog is also exposed as an MCP server (`awesome-mcp-server`) so agents can discover resources programmatically. If you add fields to the YAML schema, update:

- `src/awesome_mcp/catalog.py`
- `src/awesome_mcp/server.py`
- tests in `tests/`

## License

By contributing, you agree your commits are licensed under the repository MIT license.
