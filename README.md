# bookbot
A Python-based text analysis tool that reads `.txt` book files and generates insightful word and character frequency reports from the text.

---

## Features

- Word count analysis
- Character frequency (case-insensitive, alphabetical only)
- Pretty printed reports
- Graceful CLI interface with usage hints
- Handles missing/unreadable files
---

## Project Structure
```bash
bookbot/
├── books/ # Directory for book text files
│ └── frankenstein.txt # Example book
├── main.py # CLI entry point
├── stats.py # Analysis functions 
├── .gitignore
├── README.md
```

---

## Usage
```bash
python3 main.py books/frankenstein.txt
```
