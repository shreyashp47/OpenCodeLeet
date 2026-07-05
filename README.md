# OpenCodeLeet

> This repository was created to test the capabilities of [OpenCode](https://opencode.ai) and is for learning purposes only.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000?logo=flask)](https://flask.palletsprojects.com)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.0-7F52FF?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![Tests](https://img.shields.io/badge/Tests-unittest-8A2BE2)](https://docs.python.org/3/library/unittest.html)
[![Challenges](https://img.shields.io/badge/Challenges-60-22c55e)](https://github.com/shreyashp47/OpenCodeLeet/tree/main/challenges)
[![Live](https://img.shields.io/badge/Live-Render-46E3B7?logo=render)](https://opencodeleet.onrender.com)

A local LeetCode-style coding challenge platform supporting **Python** and **Kotlin**. Solve algorithm problems in a web editor, run code against test cases on a local server, and get instant feedback.

![Screenshot](ss/HomePage.png)

## Quick Start

```sh
pip install flask
python3 python/app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

> **Tip:** Press `Ctrl+Enter` (or `Cmd+Enter` on Mac) to run code without clicking the button.

### Kotlin (Optional)

To solve challenges in Kotlin, install the [Kotlin compiler](https://kotlinlang.org). Choose your language from the dropdown in the editor toolbar — the server will use `kotlinc` + `java -jar` to compile and run.

## Deploy to Render (Free)

[![Deploy to Render](https://img.shields.io/badge/Deploy%20to-Render-46E3B7?logo=render&logoColor=white)](https://dashboard.render.com/blueprints)

1. Push this repo to GitHub
2. Go to [dashboard.render.com/blueprints](https://dashboard.render.com/blueprints)
3. Click **New Blueprint** and connect your repo
4. The included `render.yaml` and `Dockerfile` will automatically build and deploy
5. The site is live at **[https://opencodeleet.onrender.com/](https://opencodeleet.onrender.com/)**

> **Note:** Render's free tier spins down after 15 min of inactivity. First request after idle takes ~30s to wake up.

## Features

- **Dual language support** — switch between Python and Kotlin per challenge, code saved independently per language
- **Code editor** with syntax highlighting, line numbers, bracket matching (CodeMirror with Dracula theme)
- **Server-side execution** in an isolated subprocess with a configurable timeout (default 3s)
- **Test result parsing** — results extracted from stdout markers (`ALL_TESTS_PASSED`, `TEST_FAILED:`, `ERROR:`)
- **Solution unlock** — after 3 failed attempts on a challenge, a reference solution is revealed
- **Execution timing** — elapsed time displayed per run in milliseconds
- **Auto-save** — code persisted to `localStorage` per challenge per language, survives page reloads
- **Error line highlighting** — error locations shown in the editor gutter and scrolled into view
- **Difficulty-based sidebar** — challenges grouped by Easy / Medium / Hard with color-coded badges

## Run Tests

```sh
python3 python/test_app.py
```

## Adding a Challenge

1. Create a new `.py` file in `challenges/` (e.g., `challenges/my-challenge.py`)
2. Define a `CHALLENGE` dict with the keys below
3. Restart the server — the loader picks up new files automatically

| Key | Description |
|-----|-------------|
| `id` | URL-safe slug (e.g., `"my-challenge"`) |
| `title` | Display name (e.g., `"1. My Challenge"`) |
| `difficulty` | `"Easy"`, `"Medium"`, or `"Hard"` |
| `description` | HTML string describing the problem |
| `starter_code` | Dict keyed by language — initial code the user sees |
| `solution_code` | Dict keyed by language — reference solution (unlocked after 3 fails) |
| `test_code` | Dict keyed by language — assertion harness that prints stdout markers |

Each language entry must contain complete, runnable code that prints one of these markers:
- `ALL_TESTS_PASSED`
- `TEST_FAILED: <message>`
- `ERROR: <message>`

## Challenges (60 Total)

### Easy (24)
| # | Challenge | Solution |
|---|-----------|----------|
| 1 | Two Sum | Hash Map |
| 2 | Reverse String | Two Pointers |
| 3 | Palindrome Number | Math |
| 4 | Valid Parentheses | Stack |
| 5 | Contains Duplicate | Hash Set |
| 6 | Maximum Subarray | Kadane's Algorithm |
| 7 | Move Zeroes | Two Pointers |
| 8 | Best Time to Buy and Sell Stock | Greedy |
| 9 | Climbing Stairs | Fibonacci DP |
| 10 | Single Number | XOR |
| 11 | Missing Number | XOR / Math |
| 12 | First Unique Character in a String | Hash Map |
| 13 | Roman to Integer | Hash Map |
| 14 | Longest Common Prefix | Horizontal Scan |
| 15 | Plus One | Math |
| 16 | Power of Three | Math |
| 17 | Fizz Buzz | Simulation |
| 18 | Add Binary | Math |
| 19 | Pascals Triangle | DP |
| 20 | Remove Duplicates from Sorted Array | Two Pointers |
| 21 | Sqrt(x) | Binary Search |
| 22 | Happy Number | Hash Set / Cycle Detection |
| 23 | Intersection of Two Arrays | Hash Set |
| 24 | Majority Element | Boyer-Moore Voting |

### Medium (24)
| # | Challenge | Solution |
|---|-----------|----------|
| 1 | Longest Substring Without Repeating Characters | Sliding Window |
| 2 | Three Sum | Two Pointers |
| 3 | Group Anagrams | Hash Map |
| 4 | Longest Palindromic Substring | Expand Around Center |
| 5 | Container With Most Water | Two Pointers |
| 6 | Product of Array Except Self | Prefix/Suffix |
| 7 | Coin Change | DP |
| 8 | Longest Increasing Subsequence | Patience Sorting |
| 9 | Set Matrix Zeroes | In-Place Markers |
| 10 | Rotate Image | Transpose + Reverse |
| 11 | Spiral Matrix | Boundary Traversal |
| 12 | Jump Game | Greedy |
| 13 | Unique Paths | DP |
| 14 | Word Search | DFS / Backtracking |
| 15 | Top K Frequent Elements | Hash Map + Heap |
| 16 | Sort Colors | Dutch Flag |
| 17 | Find the Duplicate Number | Floyd's Cycle |
| 18 | House Robber | DP |
| 19 | Binary Tree Level Order Traversal | BFS |
| 20 | Number of Islands | DFS |
| 21 | Subarray Sum Equals K | Prefix Sum + Hash Map |
| 22 | Find All Anagrams in a String | Sliding Window |
| 23 | Decode Ways | DP |

### Hard (12)
| # | Challenge | Solution |
|---|-----------|----------|
| 1 | Trapping Rain Water | Two Pointers |
| 2 | First Missing Positive | Cycle Sort |
| 3 | Median of Two Sorted Arrays | Binary Search |
| 4 | Sliding Window Maximum | Deque |
| 5 | Merge k Sorted Lists | Min-Heap |
| 6 | Largest Rectangle in Histogram | Stack |
| 7 | Longest Valid Parentheses | Stack / DP |
| 8 | Edit Distance | DP |
| 9 | Minimum Window Substring | Sliding Window |
| 10 | Maximal Rectangle | Stack |
| 11 | Candy | Two-Pass Greedy |
| 12 | Word Ladder | BFS |

## Project Structure

```
Dockerfile            Container image (Python 3.11 + JDK 17 + Kotlin 2.1)
render.yaml           Render Blueprint config for one-click deploy
requirements.txt      Python dependencies (Flask)
challenges/           60 .py files — one per challenge (auto-imported)
python/
├── app.py              Flask routes and server entrypoint
├── loader.py           Auto-imports challenge files, strips title numbers
├── config.py           App constants (timeout, host, port, version)
├── runner.py           Subprocess execution engine (Python + Kotlin)
├── test_app.py         Unit tests (16 tests)
└── templates/
    └── index.html      Single-page frontend (Tailwind, CodeMirror, language switcher)
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | Tailwind CSS, CodeMirror 5, FontAwesome |
| Languages | Python (built-in), Kotlin (requires `kotlinc`) |
| Testing | unittest |
| Execution | Subprocess with 3s timeout |
| Solution Reveal | After 3 failed attempts per challenge per language |

## License

This project is for educational purposes. Challenge problems are sourced from [LeetCode](https://leetcode.com/).
