"""
04_generator_expression.py

Generator expressions.
"""

numbers = (number ** 2 for number in range(1, 6))

for value in numbers:
    print(value)
