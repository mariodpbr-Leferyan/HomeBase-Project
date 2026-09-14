# Learning guide — how this project is built

This document explains the working method used throughout this project: building HomeBase myself, phase by phase, with guidance from an AI assistant (Claude, by Anthropic) acting as a mentor/co-pilot rather than as the author of the code.

## The method, phase by phase

For each phase of the [ROADMAP](ROADMAP.md), the process is:

1. **The concept gets explained first**, before any code — what's being built and why, with a simple example outside the project when useful.
2. **The AI provides the structure** (e.g. "create a `models/invoice.py` file with an `Invoice` class") without writing the whole thing.
3. **I write a first version myself.** I can always ask "how do I do X in Python" or ask for a small, isolated example — that's different from asking the AI to write the whole feature for me.
4. **The AI reviews what I wrote**, line by line when needed: what's good, what could be improved, and why — never just "this is wrong," always the reasoning behind it.
5. **We test it together** (run the server, test it on FastAPI's `/docs` page, check the result).
6. **Commit to Git** with a clear message — also practicing how to write good commit messages (see `GITHUB_WORKFLOW.md`).

## Where the "I write / AI explains more" line shifts

- **Backend/logic (Phases 1–8):** I write most of it myself, with the AI reviewing and explaining. This is where the real programming learning happens.
- **Frontend/design (Phase 9):** here it flips — the AI explains in more detail and with fuller examples, since this is my weaker area going in. I still write it, just with more upfront guidance.
- **Configuration/infrastructure (deployment, PWA, emails):** more of a "follow a recipe" part — explained in detail step by step, since these are tools/configurations rather than programming logic to internalize deeply.

## How I ask for help in a way that helps me learn more

Instead of "write me the create-invoice route," I try to ask things like:
- "I don't understand the difference between POST and PUT here, can you explain?"
- "I wrote this, what's wrong with it?" (pasting my code)
- "Give me a small, simple example of date validation in Python, I want to try applying it myself"

This keeps me in the driver's seat, with the AI as a co-pilot — not the other way around.

## Code conventions followed throughout

- **PEP 8** — Python's official style guide (variable names in `snake_case`, 4-space indentation, etc.) — deviations get flagged during review.
- **Type hints always** — e.g. `def get_invoice(id: int) -> Invoice:` — FastAPI relies on this, and it helps clarify data flow.
- **One commit = one logical change** — never mixing several different features into the same commit.
- **Comments only when the "why" isn't obvious** — clean code should explain itself most of the time; comments exist for non-obvious decisions.

## Progress log

A `docs/PROGRESS.md` file tracks each work session: what was built, questions that came up, decisions made, and time spent (including pauses). It's also useful material to talk about this project later, e.g. in a job interview.
