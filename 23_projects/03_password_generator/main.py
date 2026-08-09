"""
Password Generator

A console-based application that generates
random passwords based on user preferences.

Author: Your Name
"""

import random
import string


def display_title():
    """Display the application title."""

    print("\n" + "=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)


def get_password_length():
    """
    Ask the user for a valid password length.

    Returns:
        int: Password length.
    """

    while True:
        try:
            length = int(input("Password Length: "))

            if length >= 4:
                return length

            print("Password length must be at least 4.")

        except ValueError:
            print("Please enter a valid whole number.")


def get_yes_no(prompt):
    """
    Ask a yes/no question.

    Args:
        prompt (str): Question displayed to the user.

    Returns:
        bool: True if the answer is yes, otherwise False.
    """

    while True:

        choice = input(prompt).strip().lower()

        if choice in ("y", "yes"):
            return True

        if choice in ("n", "no"):
            return False

        print("Please enter 'y' or 'n'.")


def generate_password(length, uppercase, lowercase,
                      digits, symbols):
    """
    Generate a random password.

    Returns:
        str: Generated password.
    """

    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    """Run the Password Generator."""

    display_title()

    while True:

        length = get_password_length()

        uppercase = get_yes_no(
            "Include Uppercase Letters? (y/n): "
        )

        lowercase = get_yes_no(
            "Include Lowercase Letters? (y/n): "
        )

        digits = get_yes_no(
            "Include Numbers? (y/n): "
        )

        symbols = get_yes_no(
            "Include Special Characters? (y/n): "
        )

        password = generate_password(
            length,
            uppercase,
            lowercase,
            digits,
            symbols
        )

        if password is None:
            print(
                "\nPlease select at least one character type."
            )

        else:
            print("\nGenerated Password:")
            print(password)

        if not get_yes_no("\nGenerate another password? (y/n): "):
            print("\nThank you for using Password Generator!")
            break


if __name__ == "__main__":
    main()
