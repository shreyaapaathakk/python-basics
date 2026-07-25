"""
Using else and finally

This script demonstrates the else and finally blocks.
"""

try:
    number = int(input("Enter a number: "))
    result = 50 / number

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Please enter a valid whole number.")

else:
    print("Result:", result)

finally:
    print("Program finished.")
