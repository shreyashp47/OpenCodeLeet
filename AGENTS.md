# AGENTS.md

## Python Location
- All source, templates, and tests reside strictly in `python/`.
- No `__init__.py`; `app.py` uses `sys.path.append` at runtime for local imports.
- `loader.py` uses `importlib` to load challenge files from `../challenges/`.

## Start Web Server
```sh
pip install flask
python3 python/app.py          # http://127.0.0.1:5000 (debug mode on)
```

## Run Tests
```sh
python3 python/test_app.py     # unittest (not pytest)
```

## Code Architecture
- `config.py` — constants: timeout (3s), host, port
- `runner.py` — `CodeRunner` class: writes code to temp file, runs in subprocess, parses stdout markers
- `loader.py` — reads all `.py` files from `../challenges/`, each exporting a `CHALLENGE` dict
- `app.py` — routes only (`/` and `/run/<id>`), uses `CodeRunner` + `loader`
- `challenges/` (root) — one file per challenge, each has a `CHALLENGE` dict

## Execution Model
- User code concatenated with `challenge['test_code']` and run in a subprocess.
- **3-second timeout** — exceeding it returns "Time Limit Exceeded".
- Result parsed from stdout markers: `ALL_TESTS_PASSED`, `TEST_FAILED:`, `ERROR:`.
- Temp files cleaned up in `finally` block.

## Challenges
- Defined as individual `.py` files in `challenges/` at the repo root.
- Each file exports a `CHALLENGE` dict with keys: `id`, `title`, `difficulty`, `description`, `starter_code`, `solution_code`, `test_code`.
- Add a new challenge: create a new `.py` file in `challenges/` and restart the server.
- Order within difficulty groups is alphabetical by filename.

## Frontend
- `python/templates/index.html` — Tailwind CSS v3, CodeMirror editor, single-page app.
- Code auto-saved to `localStorage` keyed by challenge ID.
- Keyboard shortcut: `Ctrl+Enter` / `Cmd+Enter` runs code.
- Sidebar groups challenges by difficulty (`DIFFICULTY_ORDER`).
- Solution revealed after 3 failed attempts (tracked per challenge in `localStorage`).
