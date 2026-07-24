"""
The __name__ Variable

This script demonstrates the use of
if __name__ == "__main__".
"""


def greet(name):
    """Display a greeting message."""

    print(f"Hello, {name}!")


if __name__ == "__main__":
    print("This file is being run directly.")
    greet("Alice")
