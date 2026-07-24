"""
Custom Calculator Module

This module contains simple mathematical functions.
"""


def add(number1, number2):
    """Return the sum of two numbers."""
    return number1 + number2


def subtract(number1, number2):
    """Return the difference between two numbers."""
    return number1 - number2


def multiply(number1, number2):
    """Return the product of two numbers."""
    return number1 * number2


def divide(number1, number2):
    """Return the quotient of two numbers."""

    if number2 == 0:
        return "Cannot divide by zero."

    return number1 / number2
