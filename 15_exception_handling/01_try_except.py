"""
Basic Exception Handling

This script demonstrates how to handle exceptions using try and except.
"""

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Please enter a valid whole number.")
