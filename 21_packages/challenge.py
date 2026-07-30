"""
Challenge Project

Utility Package Demo

Objective:
Build and use a package containing reusable utility modules.
"""

from my_package import (
    add,
    multiply,
    roll_dice,
    say_hello,
    is_even,
)


def main():
    """Run the Utility Package Demo."""

    print("=" * 40)
    print("UTILITY PACKAGE DEMO")
    print("=" * 40)

    print(say_hello("Alice"))

    print(f"\n15 + 25 = {add(15, 25)}")
    print(f"8 × 9 = {multiply(8, 9)}")

    dice = roll_dice()
    print(f"\nDice Roll: {dice}")

    if is_even(dice):
        print("The dice roll is even.")
    else:
        print("The dice roll is odd.")


if __name__ == "__main__":
    main()
