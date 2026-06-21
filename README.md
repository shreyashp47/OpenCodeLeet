# OpenCodeLeet

A local LeetCode-style coding challenge platform built with Flask.

Solve algorithm problems in a web editor, run code against test cases on a local server, and get instant feedback — all without an internet connection.

![Screenshot](python/Screenshot%202026-06-21%20at%203.15.57%E2%80%AFPM.png)

## Features

- Code editor with syntax highlighting (CodeMirror)
- Server-side code execution with 3-second timeout
- Multiple challenges: Two Sum, Reverse String, Palindrome Number, Valid Parentheses
- Code auto-saved to `localStorage`
- Dark-themed UI (Tailwind CSS)

## Quick Start

```sh
pip install flask
python3 python/app.py
```

Open http://127.0.0.1:5000 in your browser.

## Run Tests

```sh
python3 python/test_app.py
```

## Adding a Challenge

Edit `python/challenges.py` and append a new entry to the `CHALLENGES` dict with `starter_code`, `test_code`, and `description` fields.

## Project Structure

```
├── python/
│   ├── app.py              # Flask server
│   ├── challenges.py       # Challenge definitions
│   ├── test_app.py         # Unit tests (unittest)
│   └── templates/
│       └── index.html      # Single-page frontend
└── AGENTS.md
```

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** Tailwind CSS, CodeMirror, FontAwesome
- **Testing:** unittest
