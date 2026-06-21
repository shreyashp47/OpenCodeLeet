# OpenCodeLeet

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000?logo=flask)](https://flask.palletsprojects.com)
[![Tests](https://img.shields.io/badge/Tests-unittest-8A2BE2)](https://docs.python.org/3/library/unittest.html)
[![OpenCode](https://img.shields.io/badge/OpenCode-Testing-amber)](https://opencode.ai)

A local LeetCode-style coding challenge platform built with Flask. Solve algorithm problems in a web editor, run code against test cases on a local server, and get instant feedback — all without an internet connection.

> This repository was created to test the capabilities of [OpenCode](https://opencode.ai) and is for learning purposes only.

![Screenshot](python/Screenshot%202026-06-21%20at%203.15.57%E2%80%AFPM.png)

---

## Challenges

| # | Title | Difficulty |
|---|-------|------------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Medium |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard |
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | Hard |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard |

---

## Quick Start

```sh
pip install flask
python3 python/app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

> **Tip:** Press `Ctrl+Enter` (or `Cmd+Enter` on Mac) to run code without clicking the button.

## Features

- **Code editor** with syntax highlighting, line numbers, and bracket matching (CodeMirror)
- **Server-side execution** in an isolated subprocess with a 3-second timeout
- **Test result parsing** — results extracted from stdout markers (`ALL_TESTS_PASSED`, `TEST_FAILED:`, `ERROR:`)
- **Solution unlock** — after 3 failed attempts on a challenge, a reference solution is revealed
- **`Ctrl+Enter` / `Cmd+Enter`** keyboard shortcut to run code
- **Auto-save** — code is persisted to `localStorage` per challenge, survives page reloads
- **Difficulty-based sidebar** — challenges grouped by Easy / Medium / Hard with color-coded badges
- **Execution timing** — displays elapsed time in milliseconds for each run

---

## Run Tests

```sh
python3 python/test_app.py
```

---

## Adding a New Challenge

1. Create a new `.py` file in the `challenges/` directory (e.g., `challenges/my-challenge.py`)
2. Define a `CHALLENGE` dict with:
   - `id` — URL-safe slug
   - `title` — display name
   - `difficulty` — `"Easy"`, `"Medium"`, or `"Hard"`
   - `description` — HTML string (uses existing Tailwind classes in examples)
   - `starter_code` — Python `class Solution` with method stubs
   - `solution_code` — reference solution (revealed after 3 failed attempts)
   - `test_code` — assertion-based test harness that prints `ALL_TESTS_PASSED`, `TEST_FAILED:`, or `ERROR:`
3. Restart the server — the loader picks up new files automatically

---

## Project Structure

```
├── challenges/             One file per challenge (auto-loaded)
│   ├── two-sum.py
│   ├── reverse-string.py
│   ├── palindrome-number.py
│   ├── valid-parentheses.py
│   ├── longest-substring.py
│   ├── three-sum.py
│   ├── group-anagrams.py
│   ├── trapping-rain-water.py
│   ├── first-missing-positive.py
│   └── median-two-arrays.py
├── python/
│   ├── app.py              Flask routes and server entrypoint
│   ├── loader.py           Loads all challenge files from ../challenges/
│   ├── config.py           App configuration (timeout, port, etc.)
│   ├── runner.py           Isolated subprocess code execution engine
│   ├── test_app.py         Unit tests (unittest)
│   └── templates/
│       └── index.html      Single-page frontend (Tailwind + CodeMirror)
├── AGENTS.md               OpenCode agent instructions
└── README.md
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | Tailwind CSS, CodeMirror, FontAwesome |
| Testing | unittest |
| Execution | Subprocess with 3s timeout |
| Solution Reveal | Unlocked after 3 failed attempts per challenge |

---

## License

This project is for educational purposes. Challenge problems are sourced from [LeetCode](https://leetcode.com/).
