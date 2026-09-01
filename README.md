# HomeBase — Shared Household & Financial Management

> A personal/family app to manage invoices, expenses, recurring payments, budget, a shared calendar, shopping lists, and a wishlist — all in one place.

**Project status:** 🚧 In development — planning phase (see [ROADMAP](docs/ROADMAP.md))
**Author:** [@mariodpbr-Leferyan](https://github.com/mariodpbr-Leferyan)
**Repository:** [HomeBase-Project](https://github.com/mariodpbr-Leferyan/HomeBase-Project)
**Stack:** Python (FastAPI) · PostgreSQL/SQLite · HTML/CSS/JS → PWA

---

## What is HomeBase?

HomeBase is a web application (with a planned evolution into a PWA/mobile experience) designed for a family or couple to manage, together and with the same shared data:

- 🧾 **Invoices** — record amount and issue date
- 🍽️ **Food and monthly expenses**
- 🔁 **Recurring payments** — due dates, status (paid/overdue), and alerts
- ⏰ **Alerts** — overdue payments and missing invoice records
- 👥 **Users** — multiple people managed within the same app
- 📅 **Shared calendar** — activities, tasks, appointments
- 💰 **Budget** — calculation and management of the household budget
- 🛒 **Shopping list module** (Bring!-style) — integrated
- 🎁 **Wishlist** — with direct links to stores (Amazon, Fnac, Worten, Continente, etc.)

This project starts as a **personal, experimental portfolio piece**, with the goal of later being made available publicly.

## Why this README is short

All detailed documentation lives in the [`/docs`](docs/) folder, organized by topic so it's easy to navigate and keep up to date as the project progresses:

| Document | What you'll find there |
|---|---|
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | All project phases, in order, with goals and "done" criteria |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Chosen tech stack and why (Python, framework, database, frontend) |
| [`docs/SETUP.md`](docs/SETUP.md) | How to set up the dev environment (VSCode, Python, Git) from scratch |
| [`docs/DATA_MODEL.md`](docs/DATA_MODEL.md) | Database structure — entities, relationships, fields |
| [`docs/LEARNING_GUIDE.md`](docs/LEARNING_GUIDE.md) | How we'll work on the code together, phase by phase |
| [`docs/GITHUB_WORKFLOW.md`](docs/GITHUB_WORKFLOW.md) | How to organize commits, branches, issues, and the task board |
| [`docs/PROJECT_MANAGEMENT.md`](docs/PROJECT_MANAGEMENT.md) | GitHub Projects setup, Epics, Sprints, and full backlog |
| [`CHANGELOG.md`](CHANGELOG.md) | Change history by version |

## Quick install (once the code exists)

```bash
git clone https://github.com/mariodpbr-Leferyan/HomeBase-Project.git
cd HomeBase-Project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## License

TBD (suggestion: MIT, for a public portfolio project — see `docs/ROADMAP.md` Phase 11).