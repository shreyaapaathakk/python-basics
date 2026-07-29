"""
03_basic_decorator.py

Creating a basic decorator.
"""


def decorator(function):
    """Decorator function."""

    def wrapper():
        print("Before the function executes.")
        function()
        print("After the function executes.")

    return wrapper


@decorator
def greet():
    """Print a greeting."""
    print("Hello!")


greet()
