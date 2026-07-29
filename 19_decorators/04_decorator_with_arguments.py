"""
04_decorator_with_arguments.py

Decorating functions with parameters.
"""


def decorator(function):
    """Decorator supporting arguments."""

    def wrapper(name):
        print("Starting function...")
        function(name)
        print("Function completed.")

    return wrapper


@decorator
def welcome(name):
    """Welcome a user."""
    print(f"Welcome, {name}!")


welcome("Alice")
