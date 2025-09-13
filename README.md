# AI Code Reviewer

## Project Overview
AI Code Reviewer is a Python tool that analyzes Python code files for common issues. 
It checks for syntax errors, function length, and includes a placeholder for plagiarism detection.

This project is useful for students, developers, and educators to quickly review code quality.

---

## Features
- **Syntax Check:** Detects syntax errors in Python files.
- **Function Length Check:** Flags functions that exceed a specified number of lines.
- **Plagiarism Placeholder:** Currently indicates code is plagiarism-free.
- **Folder-wide Review:** Can review all Python files in a folder and generate separate reports.
- **Reports:** Each review is saved in a timestamped file inside the `reports/` folder.

---

## Project Structure

AI_Code_Reviewer/
│
├─ main.py           # Entry point for running the AI Code Reviewer
├─ ai_reviewer.py    # Contains the CodeReviewer class and all review logic
├─ test_samples/     # Folder containing sample Python files for testing
├─ reports/          # Folder where review reports are saved
└─ README.md         # Project documentation

**Explanation of key files/folders:**

- **main.py** → Users run this file to start the code review process.  
- **ai_reviewer.py** → Contains all functions for syntax check, function length check, and plagiarism placeholder.  
- **test_samples/** → Store sample `.py` files to test your reviewer.  
- **reports/** → Automatically stores timestamped review reports.  
- **README.md** → Explains the project, how to run it, and folder structure.  

---

## How to Use

1. Open the project in **VS Code** or your preferred editor.
2. Open the terminal in the project folder.
3. Run the reviewer:

```bash
python main.py

When prompted, enter the path to a single file or a folder containing Python files:

test_samples/sample1.py


Check the console output for the review results.

Review reports are saved in the reports/ folder with timestamped filenames.

Future Enhancements

1). Integrate actual plagiarism detection.

2). Add additional code quality checks (variable naming, unused imports, complexity).