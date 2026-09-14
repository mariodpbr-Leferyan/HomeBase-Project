# Environment setup — step by step (Phase 0)

Follow this exact order. Every step explains the "why," not just the "how."

## 1. Install Python

1. Go to https://www.python.org/downloads/ and install the latest version (3.12+).
2. **Important (Windows):** in the installer, check "Add Python to PATH" — without this, the computer won't know where to find Python when you type commands.
3. Confirm it worked by opening a terminal and typing:
   ```bash
   python --version
   ```
   It should show something like `Python 3.12.x`.

## 2. Install Git and connect to GitHub

1. Install Git: https://git-scm.com/downloads
2. Set up your identity (used in every commit):
   ```bash
   git config --global user.name "Your name"
   git config --global user.email "your-email@example.com"
   ```
3. Create the empty repository on GitHub (via browser): `https://github.com/mariodpbr-Leferyan/homebase` — suggested name `homebase`, public visibility (good for a portfolio), no auto-generated README (we'll create our own).

## 3. VSCode — essential extensions

Open VSCode and install (Extensions panel, the squares icon):
- **Python** (Microsoft) — provides autocomplete, error detection, running code
- **Pylance** — further improves autocomplete and type detection
- **GitLens** — shows Git history and changes directly in the editor
- **Even Better TOML** (optional, useful for config files)

## 4. Clone/create the project locally

```bash
# Pick a folder to store your projects, e.g.:
cd Documents/Projects

git clone https://github.com/mariodpbr-Leferyan/homebase.git
cd homebase
```

## 5. Virtual environment (venv)

**What it is and why:** a "virtual environment" is an isolated folder where we install Python libraries just for this project, without mixing with other projects or the system. It avoids version conflicts between different projects.

```bash
python -m venv venv
```

Activate it (do this every time you open a new terminal to work on the project):
```bash
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```
You'll know it's active because the terminal will show `(venv)` before the path.

## 6. Install the first dependencies

With `venv` active:
```bash
pip install fastapi uvicorn sqlalchemy python-dotenv "python-jose[cryptography]" "passlib[bcrypt]"
```
Then, save the exact list of installed dependencies:
```bash
pip freeze > requirements.txt
```
This guarantees that when the project is cloned on another computer (or reviewed with AI assistance), `pip install -r requirements.txt` installs the exact same versions.

## 7. `.gitignore` file

Create a `.gitignore` file at the project root — it tells Git which files/folders should **never** be pushed to GitHub (virtual environment, config files with passwords, etc.):
```
venv/
__pycache__/
*.pyc
.env
*.db
.vscode/
```

## 8. First commit

```bash
git add .
git commit -m "chore: initial project structure"
git push origin main
```

## Phase 0 final checklist

- [ ] `python --version` works
- [ ] `homebase` repository created on GitHub
- [ ] VSCode with extensions installed
- [ ] `venv` created and active
- [ ] `requirements.txt` generated
- [ ] `.gitignore` created
- [ ] First commit made and pushed to GitHub

Once you've checked all of this, let me know and we'll move on to Phase 1 (the first real code).
