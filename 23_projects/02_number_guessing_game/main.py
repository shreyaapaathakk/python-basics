"""
Number Guessing Game

A simple console game where the player guesses
a randomly generated number.

Author: Your Name
"""

import random


def display_title():
    """Display the game title."""

    print("\n" + "=" * 40)
    print("     NUMBER GUESSING GAME")
    print("=" * 40)


def get_guess():
    """
    Get a valid guess from the user.

    Returns:
        int: User's guessed number.
    """

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))

            if 1 <= guess <= 100:
                return guess

            print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_game():
    """Run one round of the game."""

    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")

    while True:

        guess = get_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print("\nCongratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break


def play_again():
    """
    Ask the user whether to play another round.

    Returns:
        bool: True if the user wants to continue.
    """

    while True:
        choice = input("\nPlay again? (y/n): ").strip().lower()

        if choice in ("y", "yes"):
            return True

        if choice in ("n", "no"):
            return False

        print("Please enter 'y' or 'n'.")


def main():
    """Run the Number Guessing Game."""

    display_title()

    while True:

        play_game()

        if not play_again():
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
