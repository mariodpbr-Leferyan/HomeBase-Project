# GitHub workflow

## Branches

For a personal project like this you don't need a complex structure, but it's worth practicing the professional habit:

- `main` — stable code, always working
- `dev` — where you merge each phase's work before it goes to `main`
- `feature/feature-name` — one branch per feature (e.g. `feature/invoices-crud`)

Suggested flow:
```bash
git checkout dev
git checkout -b feature/invoices-crud
# ... write code, make commits ...
git push origin feature/invoices-crud
# then, on GitHub: open a Pull Request from feature/invoices-crud -> dev
```

## Commit messages (Conventional Commits)

Use this format — it's a widely recognized standard in the industry:

```
type: short lowercase description

[optional body, more detail]
```

Most common types:
| Type | When to use |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation-only changes |
| `refactor` | Reorganize code without changing behavior |
| `test` | Add/change tests |
| `chore` | Maintenance tasks (configs, dependencies) |

Examples:
```
feat: add invoice creation endpoint
fix: correct overdue payment date calculation
docs: update roadmap with phase 5 details
```

## Issues and Project Board

On GitHub, use the **Issues** tab to log tasks to do (one issue per small task, e.g. "Create Invoice model"), and the **Projects** tab to build a Kanban-style board (columns: *To Do*, *In Progress*, *Done*). This is great for a portfolio — it shows organization to anyone viewing the repository.

Suggested labels for issues:
- `phase-0`, `phase-1`, ... — so you know which phase it belongs to
- `backend`, `frontend`, `docs` — by area
- `good-first-issue` — if you ever open the project to outside collaboration

## Releases and versioning

When a major phase is complete and stable, create a GitHub release with a semantic tag:
```
v0.1.0  → end of Phase 1 (users)
v0.2.0  → end of Phase 2 (invoices)
...
v1.0.0  → first "complete" version ready for public use
```

## CHANGELOG.md

Keep a `CHANGELOG.md` at the project root, updated with every release, listing what changed — another element that adds a lot of value to a technical portfolio.
