# Architecture — HomeBase

This document explains **every technical choice and why**, so you understand the alternatives instead of just following instructions blindly.

## Overview

```
[ Browser / Phone ]
         |
         |  HTTP (requests and responses)
         v
[ FastAPI (Python) ]  <-- the "brain": receives requests, applies rules, stores/reads data
         |
         v
[ Database (SQLite -> PostgreSQL) ]
```

## 1. Backend language and framework: Python + FastAPI

**Alternatives considered:** Flask, Django, FastAPI.

| | Flask | Django | FastAPI |
|---|---|---|---|
| Learning curve | Easy | Medium/high | Easy/medium |
| Automatic API documentation | No | No (native) | **Yes, automatic** |
| Data validation | Manual | Manual/ORM | **Automatic (via type hints)** |
| Async (good for alerts, emails) | Limited | Limited | **Native** |
| Good for really learning Python | Yes | Less so (lots of "magic") | **Yes — forces you to think in types** |

**Choice: FastAPI.**
Main reason: since you'll be writing a large part of the code while learning, FastAPI forces you to explicitly declare what type each piece of data is (`str`, `int`, `float`, `date`...). That teaches you "correct" Python from the start, and on top of that it automatically generates an interactive API documentation page (at `/docs`), a great way to test things without writing a frontend first.

## 2. Database: SQLite → PostgreSQL

- **During development:** SQLite. It's a single file (`homebase.db`), nothing to install, perfect for getting started and for your personal portfolio.
- **When it goes to production/public:** PostgreSQL. More robust for multiple simultaneous users.
- **How we switch without rewriting everything:** we use an ORM (see below), a layer that translates Python into SQL — switching from SQLite to PostgreSQL barely changes the code.

## 3. ORM: SQLAlchemy

An ORM (*Object-Relational Mapper*) lets you write `Invoice(amount=50, date="2026-09-01")` instead of writing raw SQL (`INSERT INTO invoices...`). **SQLAlchemy** is the most widely used one in Python, integrates great with FastAPI, and we'll use it together with **Alembic** (a "migrations" tool — records changes to the database structure over time, like a "change history" just for the database).

## 4. Authentication: JWT (JSON Web Tokens)

When you log in, the server returns a "token" — a kind of temporary badge you present on every following request, so you don't have to send your password every time. It's the most common pattern in modern APIs. Passwords are never stored as plain text — we use a hashing function (`bcrypt`) that transforms them irreversibly.

## 5. Frontend: start with Jinja2, evolve later

- **Phase 9 (initial):** Jinja2 — a "templating" system FastAPI itself can serve, mixing HTML with Python data. Advantage: zero extra configuration, you see results in the browser from day one.
- **Later (optional):** if you want a smoother experience (no page reloads), we migrate parts to React. Not necessary for the MVP.

## 6. Path to mobile: PWA

A **PWA (Progressive Web App)** is a "normal" web app with:
- A `manifest.json` (tells the phone the app's name, icon, and color)
- A `service worker` (a small script that enables offline functionality and push notifications)

Result: the user visits the site on their phone, taps "Add to home screen," and gets an icon just like any native app — without you needing to learn Kotlin/Swift or submit to app stores.

## 7. Planned folder structure

```
homebase/
├── app/
│   ├── main.py                # application entry point
│   ├── database.py            # database connection
│   ├── models/                 # one file per entity (User, Invoice, Expense...)
│   ├── schemas/                 # API input/output shapes (validation)
│   ├── routers/                 # routes grouped by feature
│   ├── services/                 # business logic (calculations, alerts)
│   └── templates/                 # HTML (Jinja2) — from Phase 9 onward
├── tests/                      # automated tests (pytest)
├── docs/                       # this documentation
├── requirements.txt             # project dependencies
├── .env.example                 # environment variables (never commit the real .env!)
├── .gitignore
└── README.md
```

## 8. Deployment (Phase 11)

Free/low-cost options to get started: **Render**, **Railway**, or **Fly.io** — all support Python + PostgreSQL with direct deploy from GitHub. We'll pick this in more detail when we reach Phase 11.
