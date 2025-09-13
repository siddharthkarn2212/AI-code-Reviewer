from ai_reviewer import CodeReviewer

if __name__ == "__main__":
    # Load the file you want to review
    reviewer = CodeReviewer("sample_code.py")
    issues = reviewer.review_code()

    print("AI Code Reviewer Report")
    print("------------------------")
    for issue in issues:
        print(f"- {issue}")
