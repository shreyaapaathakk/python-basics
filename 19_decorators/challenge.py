"""
Challenge Project

Function Logger

Objective:
Create a decorator that logs every function call with its name and arguments.
"""


def log_calls(function):
    """Log the function name and arguments before execution."""

    def wrapper(*args, **kwargs):
        print(f"\nCalling: {function.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")

        result = function(*args, **kwargs)

        print(f"Returned: {result}")
        return result

    return wrapper


@log_calls
def multiply(a, b):
    """Multiply two numbers."""
    return a * b


@log_calls
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def main():
    """Run the Function Logger application."""
    print(multiply(6, 7))
    print(greet("Alice"))


if __name__ == "__main__":
    main()
