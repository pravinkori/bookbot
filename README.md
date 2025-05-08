# 📚 BookBot
[![bookbot test](https://github.com/pravinkori/bookbot/actions/workflows/python-app.yml/badge.svg?branch=addtests)](https://github.com/pravinkori/bookbot/actions/workflows/python-app.yml)

BookBot is a Python-based text analysis tool that reads `.txt` book files and generates insightful word and character frequency reports from the text.

## 🚀 Features

- Word count analysis
- Character frequency (case-insensitive, alphabetical only)
- Pretty printed reports
- Graceful CLI interface with usage hints
- Handles missing/unreadable files
- Automatically lists available `.txt` books if no path is provided
- Modular package-style project layout
- Unit tested using `pytest`
- CI integration with GitHub Actions

## 🗂 Project Structure
```bash
bookbot/
├── books/ # Directory for book text files
│ └── frankenstein.txt # Example book
├── src/ # Source code
│ ├── init.py
│ ├── main.py # CLI entry point
│ └── stats.py # Analysis functions
├── tests/ # Unit tests
│ ├── init.py
│ └── test_stats.py
├── .github/
│ └── workflows/
│ └── python-app.yml # GitHub Actions workflow
├── .gitignore
├── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/bookbot.git
cd bookbot
python3 -m venv venv
source venv/bin/activate
pip install pytest
```

## Running Tests
From root of the project directory run the following command in terminal:
```bash
pytest
```

## Usage
```bash
python3 src/main.py books/frankenstein.txt
```
If no book path is provided, BookBot will list all .txt files inside the books/ directory.

## GitHub Actions CI

BookBot is configured to automatically run tests on every push and pull request using GitHub Actions. See .github/workflows/python-tests.yml for details.