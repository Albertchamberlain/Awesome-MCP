## Catalog entry summary

- **Entry id(s):**
- **Kind / category:**
- **Why it belongs in Awesome-MCP:**

## Security and commercial context (required)

- **Authentication:** none / API key / OAuth / other (describe):
- **Data egress:** what data leaves the user's machine, and to which third parties?
- **Operations:** read-only / write / destructive (delete, overwrite, spend money, send messages):
- **User confirmation:** which risky actions require an explicit confirmation step?
- **Source / license:** open source (link + SPDX) / source-available / proprietary:
- **Pricing / free limits:** free forever / free tier limits / paid-only (summarize):

### Quick examples

- **Safe read-only:** a local stdio server that only lists files under a user-chosen directory, no network calls, MIT-licensed, no paid API.
- **Hosted write-capable:** a remote MCP that creates tickets in a SaaS product using an API key; may send ticket text to the vendor; free tier capped at N requests/day.

## Maintainer notes

- [ ] `official: true` is reserved for MCP steering-group / vendor-official projects. It is **not** a security review, open-source badge, or endorsement of safety.
- [ ] I ran `awesome-mcp validate`, `awesome-mcp readme`, and `pytest` after editing `data/catalog.yaml`.
- [ ] I searched the catalog first to avoid duplicates (`awesome-mcp search <name>`).
