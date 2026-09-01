# Learning guide — how we'll work

This document explains how our coding sessions will work, so you get the most out of writing most of the code yourself.

## The method, phase by phase

For each phase of the [ROADMAP](ROADMAP.md), the process is:

1. **I explain the concept** before any code — what we're building and why, with a simple example outside the project if it helps.
2. **I give you the structure** (e.g. "create a `models/invoice.py` file with an `Invoice` class") without writing the whole thing for you.
3. **You write a first version.** You can always ask "how do I do X in Python" or ask for a small, isolated example — that's different from asking me to write the whole feature.
4. **I review what you wrote**, line by line if needed: I explain what's good, what could be improved, and why — never just "this is wrong," always the reasoning.
5. **We test it together** (run the server, test it on FastAPI's `/docs` page, check the result).
6. **Commit to Git** with a clear message — you'll also learn to write good commit messages (see `GITHUB_WORKFLOW.md`).

## Where the "you write / I explain more" line shifts

- **Backend/logic (Phases 1–8):** you write most of it, with my support reviewing and explaining. This is where you want to really learn to program.
- **Frontend/design (Phase 9):** here we flip it — I explain in more detail and with fuller examples, since you said you have little knowledge in this area. You still write it, just with more upfront guidance.
- **Configuration/infrastructure (deployment, PWA, emails):** more of a "follow a recipe" part — I'll explain each step in detail, since these are tools/configurations rather than programming logic.

## How to ask for help in a way that helps you learn more

Instead of "write me the create-invoice route," try:
- "I don't understand the difference between POST and PUT here, can you explain?"
- "I wrote this, what's wrong with it?" (pasting your code)
- "Give me a small, simple example of date validation in Python, I want to try applying it myself"

This keeps you in the driver's seat, with me as a co-pilot — not the other way around.

## Code conventions we'll follow

- **PEP 8** — Python's official style guide (variable names in `snake_case`, 4-space indentation, etc.) — I'll flag deviations as you write.
- **Type hints always** — e.g. `def get_invoice(id: int) -> Invoice:` — FastAPI relies on this, and it helps you think more clearly about data.
- **One commit = one logical change** — never "mix" three different features into the same commit.
- **Comments only when the "why" isn't obvious** — clean code explains itself most of the time; comments exist for non-obvious decisions.

## Progress log

I suggest keeping a `docs/PROGRESS.md` file (we can create it when you start Phase 1) where you note, per phase, what's already working, questions that came up, and decisions made. It's also great material to talk about this project in a job interview later.
