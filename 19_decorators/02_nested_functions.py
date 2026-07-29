"""
02_nested_functions.py

Understanding nested functions.
"""


def outer():
    """Outer function."""

    def inner():
        """Inner function."""
        print("Hello from the inner function!")

    print("Inside the outer function.")
    inner()


outer()
