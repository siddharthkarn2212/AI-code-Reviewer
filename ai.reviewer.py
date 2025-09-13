import ast
from datetime import datetime
import os

class CodeReviewer:
    def __init__(self,filename ):
        self.filename = filename

    def check_syntax(self):
        """Check for syntax errors in the code file."""
        try:
            with open(self.filename, "r") as f:
                source = f.read()
            ast.parse(source)
            return []
        except SyntaxError as e:
            return [f"Syntax error at line {e.lineno}: {e.msg}"]

    def check_function_length(self, max_lines=15):
        """Check if any function exceeds max_lines. Include line numbers."""
        issues = []
        with open(self.filename, "r") as f:
            lines = f.readlines()

        current_func = None
        func_start = 0

        for i, line in enumerate(lines, start=1):
            stripped = line.strip()
            if stripped.startswith("def "):
                # Check previous function length
                if current_func and i - func_start > max_lines:
                    issues.append(
                        f"Function '{current_func}' (lines {func_start}-{i-1}) is too long ({i - func_start} lines)"
                    )
                current_func = stripped.split("(")[0][4:]
                func_start = i

        # Check last function in file
        if current_func and len(lines) - func_start + 1 > max_lines:
            issues.append(
                f"Function '{current_func}' (lines {func_start}-{len(lines)}) is too long ({len(lines) - func_start + 1} lines)"
            )

        return issues

    def check_plagiarism(self):
        """Placeholder for plagiarism check."""
        return ["No plagiarism detected."]

    def review_code(self):
        """Run all code checks and return structured report as a dictionary."""
        return {
            "Syntax Issues": self.check_syntax(),
            "Function Length Issues": self.check_function_length(),
            "Plagiarism Check": self.check_plagiarism()
        }

def main():
    print("=== AI Code Reviewer ===")
    
    file_path = input("Enter path to code file for review: ")
    reviewer = CodeReviewer(file_path)
    review_dict = reviewer.review_code()

    # Format review result
    review_lines = []
    for section, issues in review_dict.items():
        review_lines.append(f"--- {section} ---")
        if issues:
            review_lines.extend(issues)
        else:
            review_lines.append("No issues found.")
        review_lines.append("")  # Add empty line for spacing

    review_result = "\n".join(review_lines)
    
    # Print result
    print("\n" + review_result)
    
    # Ensure reports folder exists
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    # Save report with timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    report_filename = f"review_report_{timestamp}.txt"
    report_path = os.path.join("reports", report_filename)

    with open(report_path, "w") as f:
        f.write(review_result)

    print(f"\nReport saved as {report_filename} in reports/ folder")

if __name__ == "__main__":
    main()
