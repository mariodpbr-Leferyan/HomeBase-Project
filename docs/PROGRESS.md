# Progress Log — HomeBase

This log tracks work sessions on the project: what was done, time spent, and pauses. Entries are added chronologically, most recent at the bottom. Time and pause data is self-reported by the developer at the start/end of each session, since durations can't be tracked automatically.

**How to use this log each session:**
- At the start: state the date and, if resuming after a break, roughly how long the pause was.
- At the end: a short summary gets added of what was accomplished.

---

## Session 1 — September 1, 2026

**Phase:** 0 (Setup) → started Phase 1 (Foundation)

**What was done:**
- Installed Python, confirmed version
- Installed Git, configured identity
- Created `HomeBase-Project` repository on GitHub
- Installed VSCode extensions (Python, Pylance, GitLens)
- Fixed folder structure issues (nested zip extraction, `venv` in wrong location)
- Created and activated `venv`, installed base dependencies, generated `requirements.txt`
- Created `.gitignore`, resolved duplicate/incorrectly named file
- First commit and push to GitHub (via OAuth browser login)
- Set up GitHub Projects board (`HomeBase Roadmap`): Epic, Sprint, Priority fields; Board and Table views; repository labels
- Created Sprint 0 issues (retroactively marked Done) and Sprint 1 issues (To Do)
- Wrote first FastAPI code: `app/main.py` with a `/health` route
- Hit and resolved a broken `venv` (stale Python path from folder move) — recreated it in the correct location
- Confirmed the server runs and `/health` + `/docs` respond correctly

**Status at end of session:** Phase 0 complete. Phase 1 started — first working route confirmed via FastAPI's `/docs` page. Progress committed and pushed to GitHub.

**Pause after this session:** untracked/unknown duration (flagged retroactively as inaccurate — see Session 2 note).

---

## Session 2 — September 8, 2026

**Resumed after:** an unspecified pause (longer than the initially assumed 7 days — exact length not tracked, per developer note). Starting this session, pause/resume durations will be reported explicitly going forward.

**What was done so far this session:**
- Set up this progress-tracking system and file
- Reviewed session start checklist (venv active, `/health` confirmed working)
- Explained SQLAlchemy setup concepts (engine, session, Base)
- Provided `app/database.py` boilerplate (connection to SQLite via SQLAlchemy)
- Started `Household` model (`app/models/household.py`) — columns left as an exercise, not yet completed
- Clarified a normal `404 Not Found` on `/favicon.ico` (expected, no action needed)

**Pause flagged at 13:44** — resumed at 15:52. **Pause duration: 2h 08min.**

**What was done after resuming (15:52 → 17:48, ~1h 56min):**
- Explained `database.py` line by line (engine, session factory, Base, `get_db` dependency pattern)
- Explained `Column(TYPE, options)` syntax in detail, including `String(255)` length argument
- Introduced the term "Pythonic" and agreed to always show the most Pythonic version first, plus one alternative, going forward
- Wrote and debugged `app/models/household.py` together (fixed typos: `Strings`→`String`, `DataTime`→`DateTime`; removed invalid import line; fixed trailing commas creating tuples instead of assignments; fixed `:` vs `=` on `created_at`)
- Verified the model imports cleanly (`python -c "from app.models.household import Household..."`)
- Updated `app/main.py` to import `Household` and call `Base.metadata.create_all(bind=engine)` on startup
- Verified `homebase.db` was created and the `households` table exists (via a temporary `check_db.py` script)
- Discussed options to view the SQLite database visually (VSCode extension vs. DB Browser for SQLite vs. CLI) — recommended VSCode "SQLite Viewer" extension
- Updated Sprint status on GitHub Projects board (done by developer)

**Session 2 end: 17:48.**

**Status at end of session:** `Household` model complete and verified against the live database. Ready to start the `User` model next (password hashing, foreign key to `Household`).

**Reminder for next session start:** ✅ GitHub Projects board was updated this session — keep doing this at the end of every session (mark completed issues as Done, move next task to In Progress) so the board stays an accurate record.

---

## Session 3 — September 10, 2026

**Resumed at:** 13:12. **Pause since last session: 1 day, 19h 24min** (Sept 8, 17:48 → Sept 10, 13:12).

**What was done so far this session:**
- Explained foreign keys and password hashing concepts
- Provided `app/security.py` (hash_password / verify_password using passlib/bcrypt)
- Wrote and debugged `app/models/user.py` together — recurring mistakes caught and corrected: `:` vs `=` for field assignment (same issue as Household, now should be internalized), `Foreignkey`→`ForeignKey`, `integer`→`Integer`, `String=(255)`→`String(255)`, `class User(Base)=`→`class User(Base):`, PEP 8 spacing around `=` in keyword arguments
- Learned a VSCode regex Find & Replace trick to batch-fix `:` → `=` issues
- Learned how to manage multiple terminals in VSCode (dropdown switch, split view, keyboard cycling)
- Verified `User` model imports cleanly

**Lunch break flagged at 14:29** — resumed at 15:23. **Break duration: 54min.**

**What was done after resuming (15:23 → pause):**
- VSCode split-pane navigation shortcuts (Ctrl+1/Ctrl+2, Ctrl+K then arrow)
- Fixed `main.py`: added imports for `User`, removed an accidentally duplicated `class User(Base):` definition that had been pasted directly into `main.py` (should only ever live in `app/models/user.py` — one source of truth per class)
- Verified both `households` and `users` tables now exist in `homebase.db`
- Introduced Pydantic schemas concept (why input/output shapes differ from the DB model)
- Provided `app/schemas/user.py` (`UserCreate`, `UserResponse` — response deliberately excludes `password_hash`)
- Installed `email-validator` dependency for `EmailStr`
- Explained what `__init__.py` does (marks a folder as an importable package)

**Pause flagged at 16:10** — resumed at 16:37. **Pause duration: 27min.**

**What was done after resuming (16:37 → 17:0x, session end):**
- Explained FastAPI's `APIRouter` pattern and why routes get split into `app/routers/`
- Provided `app/routers/users.py` skeleton (router setup, dependency injection via `Depends(get_db)`)
- Wrote and completed the `POST /users/register` route together (hash password → build `User` → `db.add/commit/refresh` → `return`)
- Wired the router into `app/main.py` via `app.include_router(users.router)`
- Debugged a chain of real issues to get registration working end-to-end:
  - Typo `HTTTPException` → `HTTPException`
  - Duplicate `class User(Base):` accidentally pasted directly into `main.py` (removed — one source of truth per model)
  - `UserResponse` schema incorrectly included a `password` field (removed — this was actively leaking data in responses)
  - Typo `has_password` → `hash_password`, and broken `verify_password` logic (`.verify.hash(...)` → `.verify(...)`) in `app/security.py`
  - Version incompatibility between `passlib` and newer `bcrypt` (`AttributeError: module 'bcrypt' has no attribute '__about__'`) — resolved by pinning `bcrypt==4.0.1` in `requirements.txt`, discussed why pinning a dependency version is the correct professional fix vs. editing third-party library internals directly
- Created and used a temporary `seed_household.py` script to insert a test household (id=1) so registration could be tested before a real `POST /households` route exists
- **Successfully tested `POST /users/register` end-to-end** — 200 OK, user created with hashed password, response correctly excludes password fields

**Session 3 end.**

**Status at end of session:** Registration route fully working and verified. `Household` and `User` models, database connection, password hashing, and the first "write" endpoint are all complete and tested.

**Reminders for next session:**
- ✅ Update GitHub Projects board: mark "Create POST /users/register route" as Done, move "Create POST /auth/login route" to In Progress
- ✅ Committed and pushed
- `check_db.py` deleted; **`seed_household.py` intentionally kept** as a dev utility for testing — flagged for removal once a real `POST /households` route exists (don't forget this one, it's not part of the actual app)
- Next task: `POST /auth/login` route (JWT), then route protection middleware

**Session 3 closed at 18:04.**

---

## Session 4 — October 14, 2026

**Resumed at:** 17:25. **Pause since last session: 3 days, 23h 21min** (Sept 10, 18:04 → Sept 14, 17:25).

**What was done so far this session:**

*(To be continued as the session progresses — update this section before closing out.)*

---
