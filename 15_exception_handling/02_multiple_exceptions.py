"""
Handling Multiple Exceptions

This script demonstrates how to handle different types of exceptions.
"""

try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter a whole number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
