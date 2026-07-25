"""
Raising Exceptions

This script demonstrates how to raise exceptions manually.
"""


def check_age(age):
    """
    Check whether the age is valid.
    """

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age accepted.")


try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError as error:
    print("Error:", error)
