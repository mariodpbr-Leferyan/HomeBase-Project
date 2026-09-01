# Project Management — GitHub Projects (Scrum/Kanban)

This document explains how to set up and use GitHub Projects to manage HomeBase, and contains the full backlog (tasks) organized by Epic and Sprint.

## Why GitHub Projects instead of a separate board

GitHub Projects (the "new" version, native to GitHub) already supports:
- Kanban board (Backlog / To Do / In Progress / Review / Done columns)
- Custom fields (Epic, Priority, Sprint)
- Direct links to Issues and Pull Requests in your repository — when you close a PR, the task moves automatically
- Different views of the same data (Board, Table, Roadmap by dates)

In other words, the "board" and the "code" live in the same place, which is exactly what a recruiter wants to see in a portfolio: commit history linked to concrete tasks.

---

## Part 1 — Initial setup (do once)

### 1.1. Create the Project

1. In your GitHub repository (`homebase`), go to the **Projects** tab (next to Code, Issues, Pull requests).
2. Click **New project**.
3. Choose the **Board** template.
4. Suggested name: `HomeBase Roadmap`.

### 1.2. Create custom fields

Inside the Project, click the **+** next to the column headers (or "..." → *Settings* → *Fields*) and create:

| Field | Type | Values |
|---|---|---|
| **Status** | Single select (default) | Backlog, To Do, In Progress, In Review, Done |
| **Epic** | Single select | Epic 1 – Foundation, Epic 2 – Core Finance, Epic 3 – Household Organization, Epic 4 – Interface & Design, Epic 5 – Notifications & Mobile, Epic 6 – Launch, Epic 7 – Internationalization |
| **Sprint** | Single select | Sprint 0, Sprint 1, Sprint 2, ... Sprint 12 (use the names/dates from the `ROADMAP.md` table) |
| **Priority** | Single select | Must-have, Nice-to-have |

### 1.3. Create labels in the repository (to link to Issues)

Under **Issues → Labels → New label**, create one label per Epic (e.g. `epic-1-foundation`, `epic-2-finance`...) and one per phase (`phase-0`, `phase-1`...). This was already suggested in `GITHUB_WORKFLOW.md` — now we'll use it in practice.

### 1.4. Create Views

Create at least two views inside the Project (the "+ New view" button at the top):
- **Board by Sprint** — Kanban-style view, grouped by `Status`, filtered by the current `Sprint` (this is the one you use day to day).
- **Table by Epic** — table view, grouped by `Epic`, to see overall project progress.

---

## Part 2 — How to create and use an Issue (task)

Each line in the backlog below (Part 3) should become an **Issue** on GitHub:

1. **Issues → New issue**
2. Short, clear title (e.g. "Create User model with password hashing")
3. Description: what needs to be done, and a checklist if it makes sense
4. Assign the Epic and Phase labels
5. In the right sidebar, under **Projects**, add it to the `HomeBase Roadmap` project
6. Inside the Project, set the `Epic`, `Sprint`, `Priority` fields, and `Status = Backlog`

When you start working on it: change `Status` to `In Progress`. Once the code is done and tested: `In Review` (even solo, it's a good habit to review before marking it complete). Once committed: `Done`.

**Real-world flow tip:** you can create the branch and the Issue at the same time — on GitHub, when opening an Issue, there's a "Create a branch" button that automatically links the branch to that Issue.

---

## Part 3 — Full backlog (tasks by Sprint)

Use this list to create the Issues. You don't need to create them all at once — I suggest creating the current sprint's + the next one's, so you don't spend more time managing tasks than writing code.

### Sprint 0 — Setup (Sep 1–7) · Epic 1
- [ ] Install Python and confirm version
- [ ] Install Git and configure identity
- [ ] Create `homebase` repository on GitHub
- [ ] Install VSCode extensions (Python, Pylance, GitLens)
- [ ] Create virtual environment (`venv`) and activate it
- [ ] Install base dependencies and generate `requirements.txt`
- [ ] Create `.gitignore`
- [ ] First commit and push

### Sprint 1 — Authentication/Users (Sep 8–21) · Epic 1
- [ ] Set up database connection (SQLAlchemy + SQLite)
- [ ] Create `Household` model
- [ ] Create `User` model (with password hashing via passlib/bcrypt)
- [ ] Create `POST /users/register` route
- [ ] Create `POST /auth/login` route (returns JWT)
- [ ] Middleware/dependency to protect routes with a token
- [ ] Test full flow via FastAPI's `/docs`
- [ ] Commit + update `docs/PROGRESS.md`

### Sprint 2 — Invoices (Sep 22–28) · Epic 2
- [ ] Create `Invoice` model
- [ ] `POST /invoices` route (create)
- [ ] `GET /invoices` route (list, filtered by household)
- [ ] `PUT /invoices/{id}` and `DELETE /invoices/{id}` routes
- [ ] Test full CRUD

### Sprint 3 — Expenses (Sep 29–Oct 5) · Epic 2
- [ ] Create `Expense` model + categories
- [ ] CRUD routes
- [ ] Aggregation endpoint: total by month/category

### Sprint 4 — Recurring payments + Alerts (Oct 6–19) · Epic 2
- [ ] Create `RecurringPayment` model
- [ ] Logic to calculate the next due date
- [ ] Automatic status change logic (pending → overdue)
- [ ] Endpoint/logic for missing-invoice alerts
- [ ] Alerts visible within the app (`/alerts` endpoint)

### Sprint 5 — Budget (Oct 20–26) · Epic 2
- [ ] Create `Budget` model
- [ ] Logic: planned vs. actual spend (uses Invoices/Expenses data)
- [ ] Budget summary endpoint by category/month

### Sprint 6 — Calendar (Oct 27–Nov 2) · Epic 3
- [ ] Create `Event` model
- [ ] CRUD routes
- [ ] Date-range filter (week/month)

### Sprint 7 — Shopping (Nov 3–9) · Epic 3
- [ ] Create `ShoppingList` and `ShoppingItem` models
- [ ] CRUD routes + "mark as bought" endpoint

### Sprint 8 — Wishlist (Nov 10–16) · Epic 3
- [ ] Create `WishlistItem` model
- [ ] CRUD routes
- [ ] URL validation

### Sprint 9–10 — Frontend/Design (Nov 17–Dec 7) · Epic 4
- [ ] Set up Jinja2 in FastAPI
- [ ] Login/registration page
- [ ] Main dashboard
- [ ] Pages: invoices, expenses, calendar, shopping, wishlist
- [ ] Simple design system (colors, reusable components)
- [ ] Show visual alerts in the interface

### Sprint 11 — Notifications/PWA (Dec 8–21) · Epic 5
- [ ] Set up email sending (SMTP or free service)
- [ ] Trigger emails for payment/invoice alerts
- [ ] Create `manifest.json`
- [ ] Create a basic service worker
- [ ] Test PWA installation on a phone

### Sprint 12 — Testing + Deploy (Dec 22–Jan 4) · Epic 6
- [ ] Write tests (pytest) for authentication
- [ ] Write tests for budget and alerts
- [ ] Choose and configure a deployment platform (Render/Railway/Fly.io)
- [ ] Set up production environment variables
- [ ] Final deploy + test in production
- [ ] Update README with the live app link

### Future — Internationalization (PT) · Epic 7
- [ ] Set up translation structure
- [ ] Translate interface text
- [ ] Language selector

---

## Part 4 — Next steps (Jira)

Once you've had GitHub Projects running for a sprint or two and feel comfortable with the flow (Issues, board, status), we'll set up the same backlog in Jira — by then you'll already understand the concepts (Epic, Sprint, Backlog), and it'll just be learning a different interface, not the concepts again. Let me know when you'd like to move on to that part.
