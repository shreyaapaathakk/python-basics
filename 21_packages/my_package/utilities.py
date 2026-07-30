"""
utilities.py

Utility functions.
"""

import random


def roll_dice():
    """Return a random number between 1 and 6."""
    return random.randint(1, 6)


def is_even(number):
    """Return True if the number is even."""
    return number % 2 == 0
