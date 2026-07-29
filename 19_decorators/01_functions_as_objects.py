"""
01_functions_as_objects.py

Functions are first-class objects in Python.
"""


def greet():
    """Print a greeting."""
    print("Hello, Python!")


message = greet

message()
greet()
