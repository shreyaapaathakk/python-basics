"""
03_generators.py

Generator functions.
"""


def countdown(start):
    """Yield numbers from start to 1."""

    while start > 0:
        yield start
        start -= 1


for number in countdown(5):
    print(number)
