"""
05_multiple_decorators.py

Using multiple decorators.
"""


def stars(function):
    """Print stars before and after a function."""

    def wrapper():
        print("*" * 30)
        function()
        print("*" * 30)

    return wrapper


def title(function):
    """Print a title before calling a function."""

    def wrapper():
        print("Python Decorators")
        function()

    return wrapper


@stars
@title
def display():
    """Display a message."""
    print("Learning decorators!")


display()
