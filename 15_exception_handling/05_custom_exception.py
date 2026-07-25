"""
Custom Exceptions

This script demonstrates how to create a custom exception.
"""


class InvalidPasswordError(Exception):
    """
    Custom exception for invalid passwords.
    """


password = input("Enter a password: ")

try:
    if len(password) < 8:
        raise InvalidPasswordError(
            "Password must contain at least 8 characters."
        )

    print("Password accepted.")

except InvalidPasswordError as error:
    print("Error:", error)
