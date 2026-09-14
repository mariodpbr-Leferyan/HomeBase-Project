# Roadmap — HomeBase

This document is the full map of the project, from zero to launch. Each phase has:
- **Goal** — what we'll be able to do by the end of the phase
- **What it involves** — the technical pieces to build
- **Done criteria** — how we know it's ready to move on
- **Who writes what** — what's mine to write myself (with AI guidance) and what's more infrastructure/configuration

Order matters: each phase builds on the previous one. Don't skip phases, even if they seem "boring" — Phases 0 and 1, for example, are the foundation for everything else.

---

## Phase 0 — Environment and repository setup
**Goal:** get your computer and GitHub ready to start coding.

What it involves:
- Install Python and configure VSCode (see `SETUP.md`)
- Create the GitHub repository (`homebase`)
- Set up the virtual environment (`venv`) and the first `requirements.txt`
- Initial project folder structure
- First commit ("chore: initial project structure")

**Done when:** you can run `python --version`, `git status`, and open the project in VSCode with no errors, and the repository exists on GitHub with this `README.md` and the `docs/` folder.

**You write:** no "code" yet — but everything gets set up with step-by-step AI guidance.

---

## Phase 1 — Backend foundation: server and users
**Goal:** have a Python server running, with a working login/user system.

What it involves:
- Install and understand FastAPI (the "skeleton" that receives requests and returns responses)
- Create the first route (`/` or `/health`) just to confirm the server runs
- Connect the database (SQLite for now — a local file, no extra install)
- `User` data model (name, email, password, role within the "household")
- User registration and login (encrypted password, never stored in plain text)
- The "Household" concept — all users in a household share the same data

**Done when:** you can create a user via the API, log in, and receive a valid token.

**You write:** the models (`models/user.py`), the registration/login routes, with a line-by-line explanation of what a model is, what a route is, and why passwords are never stored in plain text.

---

## Phase 2 — Invoices
**Goal:** create, list, and view invoices.

What it involves:
- `Invoice` model (amount, issue date, category, who registered it, status)
- CRUD routes (Create, Read, Update, Delete) — the four basic operations in any app
- Linking the invoice to the household (shared data)
- Simple tests to confirm everything works

**Done when:** you can create, view, edit, and delete an invoice, and it only shows up for users of the same household.

**You write:** the `Invoice` model and the CRUD routes, with an explanation of each HTTP verb (GET, POST, PUT, DELETE) and what "CRUD" means.

---

## Phase 3 — Food and monthly expenses
**Goal:** log everyday expenses, grouped by category and month.

What it involves:
- `Expense` model (amount, category, date, description)
- Predefined categories (food, transport, leisure, etc.) — configurable
- Simple aggregations: total per month, total per category

**Done when:** you can log an expense and see the total spent this month, by category.

**You write:** the `Expense` model, the routes, and the aggregation logic (sums and grouping) — a good introduction to more advanced queries.

---

## Phase 4 — Recurring payments and alerts
**Goal:** manage recurring payments (rent, subscriptions, etc.), with due dates and overdue alerts.

What it involves:
- `RecurringPayment` model (name, amount, frequency, due day, status)
- Logic to calculate the next due date
- Status system: paid / pending / overdue
- Alert engine (Phase 4a: in-app; Phase 4b: email; Phase 4c: push — see Phase 8)
- Alert for missing invoice records (e.g. "no invoice logged in X days")

**Done when:** a recurring payment automatically switches to "overdue" once the due date passes, and a visible alert appears in the app.

**You write:** the model, the date-calculation logic (using the `datetime` library), and the alert rules.

---

## Phase 5 — Budget
**Goal:** set a monthly/per-category budget and track actual spend against it.

What it involves:
- `Budget` model (category, limit amount, period)
- Automatic calculation: planned vs. actual spend (uses data from Phases 2 and 3)
- Simple visual indicators (e.g. 70% of the "food" budget used)

**Done when:** you can set a monthly limit per category and see, in real time, how much has been spent against it.

**You write:** the model and the calculation logic — mostly "putting pieces together" from earlier phases, a good phase to see the project gain coherence.

---

## Phase 6 — Shared calendar
**Goal:** a common agenda for all users in the household.

What it involves:
- `Event` model (title, type — activity/task/appointment, date/time, created by)
- CRUD routes
- Day/week/month view on the frontend (Phase 9)

**Done when:** every user in the same household sees the same events, and can create/edit/delete them.

**You write:** the model and routes — you repeat the CRUD pattern already trained in Phases 2 and 3, now with more confidence.

---

## Phase 7 — Shopping module (Bring!-style)
**Goal:** a shared shopping list, like an "app within the app."

What it involves:
- `ShoppingList` and `ShoppingItem` models (name, quantity, bought yes/no, who added it)
- CRUD routes + an endpoint to "mark as bought"
- (Optional, more advanced) real-time updates via WebSockets

**Done when:** two users in the same household see the list update when one of them marks an item as bought.

**You write:** the model and routes; the WebSocket part is an optional extra, introduced only if you want to go further.

---

## Phase 8 — Wishlist
**Goal:** a list of "things to buy in the future," with a direct link to the store.

What it involves:
- `WishlistItem` model (name, link, estimated price, priority, store)
- CRUD routes
- Simple link validation (is it a valid URL?)

**Done when:** you can add an item with a link (e.g. Amazon), and clicking it opens the product page.

**You write:** the model, routes, and the URL validation function.

---

## Phase 9 — Frontend and design (explained step by step)
**Goal:** turn the API (which only returns data) into a usable visual interface.

What it involves (the focus here shifts to guided explanation, since this is your least confident area):
- Approach choice: simple templates (Jinja2, built into FastAPI) vs. a separate frontend (React)
  — recommendation: start with Jinja2 + HTML/CSS to see everything working quickly, migrate to React later only if you want a more "app-like" experience
- Page structure: login, dashboard, invoices, expenses, calendar, shopping, wishlist
- A simple design system (colors, typography, reusable components)
- Visual alerts (badges, on-screen notifications)

**Done when:** you can navigate every feature through the browser, without using technical tools (Postman, etc.)

**You write:** the simplest HTML/CSS with line-by-line AI support; the frontend architecture part is explained in more detail by the AI, given the lower starting confidence in this area.

---

## Phase 10 — Email and push notifications (PWA)
**Goal:** fulfill the requirement of email and mobile push alerts.

What it involves:
- Email: sent via simple SMTP or a free service (e.g. Mailgun/Brevo) for payment and invoice alerts
- PWA: manifest.json + service worker — turns the web app into something installable on a phone
- Push notifications: via the Web Push API (more advanced, done last)

**Done when:** you receive a real email alert when a payment becomes overdue, and can "install" the app on your phone's home screen.

**You write:** the alert-triggering logic (when to send); the PWA configuration is explained more step by step.

---

## Phase 11 — Testing, final documentation, and launch
**Goal:** get the project ready for a portfolio and, later, public use.

What it involves:
- Automated tests (pytest) on critical parts (authentication, budget calculation, alerts)
- API documentation (FastAPI generates this almost automatically — see ARCHITECTURE.md)
- Open-source license, `CONTRIBUTING.md`
- Deployment (e.g. Render, Railway, Fly.io — all have free tiers)
- Custom domain (optional)

**Done when:** the app is live, accessible via a link, with complete documentation on GitHub.

---

## Phase 12 (future) — Internationalization (Portuguese)
**Goal:** make the app available in Portuguese, keeping English as the base language.

What it involves:
- Translation structure (`.json` files or the `gettext`/`Babel` library)
- Language selector in the interface

Deliberately left for after everything works in English — translating too early duplicates work every time text changes.

---

## Visual phase summary

| Phase | Name | Main focus |
|---|---|---|
| 0 | Setup | Environment and GitHub |
| 1 | Users | Backend + Auth |
| 2 | Invoices | CRUD |
| 3 | Expenses | CRUD + aggregations |
| 4 | Recurring payments | Date logic + alerts |
| 5 | Budget | Calculation |
| 6 | Calendar | Shared CRUD |
| 7 | Shopping | CRUD + real time (optional) |
| 8 | Wishlist | CRUD + validation |
| 9 | Frontend/Design | Visual interface |
| 10 | Notifications | Email + PWA/Push |
| 11 | Testing + Deploy | Launch |
| 12 | Portuguese | Internationalization |
