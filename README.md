# AI Code Reviewer

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A simple AI-based Python tool to automatically review code for:
- **Syntax errors**
- **Oversized functions**

This project demonstrates the use of Python for static code analysis and is designed with extensibility in mind.

---

## 📌 Features
- Detects and reports syntax errors in Python files.
- Identifies functions exceeding a defined size threshold.
- Generates human-readable reports inside the `Reports/` folder.
- Modular design: review logic is separated (`ai.reviewer.py`) from the main entry script (`main.py`).

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries Used:** `ast`, `os`, `sys` (no heavy dependencies)

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/siddharthkarn2212/AI-code-Reviewer.git
   cd AI-code-Reviewer
2. Run the reviewer on a test file:

python main.py sample_testing.py

3. Check results inside the Reports/ folder.


📂 Project Structure

AI-code-Reviewer/
│
├── Reports/              # Stores generated reports
├── ai.reviewer.py        # Core review logic
├── main.py               # Entry point for execution
├── sample_testing.py     # Example file to test reviewer
└── README.md             # Documentation
 


 📑 Future Improvements
 1. Extend error coverage beyond syntax and size.
 2. More types of checks (unused variables, complexity, etc.).
 3. Integrate with GitHub Actions for automated code reviews.

📜 License

This project is licensed under the MIT License.


👨‍💻 About

Author: Siddharth Karn
Year: 2025
Contact: siddharthkarn1204@gmail.com


