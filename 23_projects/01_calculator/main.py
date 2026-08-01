"""
Calculator Project

A menu-driven calculator application that performs
basic arithmetic operations.

Author: Your Name
"""

def display_menu():
    """Display the calculator menu."""

    print("\n" + "=" * 40)
    print("      PYTHON CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation")
    print("8. Exit")


def get_numbers():
    """
    Get two numbers from the user.

    Returns:
        tuple: Two floating-point numbers.
    """

    while True:
        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
            return first_number, second_number

        except ValueError:
            print("Invalid input. Please enter numeric values.")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers."""

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def floor_divide(a, b):
    """Return the floor division result."""

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a // b


def modulus(a, b):
    """Return the remainder."""

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a % b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def main():
    """Run the calculator."""

    while True:

        display_menu()

        choice = input("\nEnter your choice (1-8): ")

        if choice == "8":
            print("\nThank you for using the calculator!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("Invalid choice. Please try again.")
            continue

        number1, number2 = get_numbers()

        try:

            if choice == "1":
                result = add(number1, number2)

            elif choice == "2":
                result = subtract(number1, number2)

            elif choice == "3":
                result = multiply(number1, number2)

            elif choice == "4":
                result = divide(number1, number2)

            elif choice == "5":
                result = floor_divide(number1, number2)

            elif choice == "6":
                result = modulus(number1, number2)

            else:
                result = power(number1, number2)

            print(f"\nResult: {result}")

        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()
