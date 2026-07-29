"""
01_lambda.py

Using lambda functions.
"""

# Regular function
def square(number):
    """Return the square of a number."""
    return number ** 2


print(square(5))

# Lambda function
square_lambda = lambda number: number ** 2

print(square_lambda(5))
