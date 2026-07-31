"""
Challenge Project

Project Environment Setup Guide

Objective:
Create a reusable checklist for setting up a new Python project with a virtual environment.
"""


def display_setup_steps():
    """Display the recommended setup steps for a new project."""

    steps = [
        "1. Create a project folder.",
        "2. Open a terminal in the project folder.",
        "3. Create a virtual environment: python -m venv venv",
        "4. Activate the virtual environment.",
        "5. Install required packages using pip.",
        "6. Verify installed packages with pip list.",
        "7. Generate requirements.txt using pip freeze.",
        "8. Add 'venv/' to .gitignore.",
        "9. Commit your project files (excluding venv).",
        "10. Share requirements.txt with collaborators.",
    ]

    print("=" * 50)
    print("NEW PYTHON PROJECT SETUP")
    print("=" * 50)

    for step in steps:
        print(step)


def main():
    """Run the Project Environment Setup Guide."""
    display_setup_steps()


if __name__ == "__main__":
    main()
