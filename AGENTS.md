# AGENTS.md

## Python Location
- All source, templates, and tests reside strictly in `python/`.
- No `__init__.py`; `app.py` uses `sys.path.append` at runtime for imports.

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
- `app.py` — routes only (`/` and `/run/<id>`), uses `CodeRunner`
- `challenges.py` — static `CHALLENGES` dict + `DIFFICULTY_ORDER` list

## Execution Model
- User code concatenated with `challenge['test_code']` and run in a subprocess.
- **3-second timeout** — exceeding it returns "Time Limit Exceeded".
- Result parsed from stdout markers: `ALL_TESTS_PASSED`, `TEST_FAILED:`, `ERROR:`.
- Temp files cleaned up in `finally` block.

## Challenges
- Defined in `python/challenges.py` as a dict keyed by slug.
- Each challenge has: `starter_code` (always a `class Solution`), `test_code` (assert-based), HTML `description`, and `difficulty`.
- Add new challenges by appending to `CHALLENGES` dict (order within difficulty groups is insertion order).

## Frontend
- `python/templates/index.html` — Tailwind CSS v3, CodeMirror editor, single-page app.
- Code auto-saved to `localStorage` keyed by challenge ID.
- Keyboard shortcut: `Ctrl+Enter` / `Cmd+Enter` runs code.
- Sidebar groups challenges by difficulty (`DIFFICULTY_ORDER`).
