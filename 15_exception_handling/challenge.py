"""
Mini Project: Safe Calculator

Concepts Used:
- Exception handling
- Loops
- Functions
- User input
"""


def calculate(number1, number2, operator):
    """
    Perform a mathematical operation.
    """

    if operator == "+":
        return number1 + number2

    if operator == "-":
        return number1 - number2

    if operator == "*":
        return number1 * number2

    if operator == "/":
        if number2 == 0:
            raise ZeroDivisionError(
                "Cannot divide by zero."
            )

        return number1 / number2

    raise ValueError("Invalid operator.")


while True:
    print("\n===== Safe Calculator =====")

    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        operator = input("Enter (+, -, *, /): ")

        result = calculate(
            first_number,
            second_number,
            operator
        )

    except ValueError as error:
        print("Error:", error)

    except ZeroDivisionError as error:
        print("Error:", error)

    else:
        print("Result:", result)

    choice = input("\nPerform another calculation? (y/n): ").lower()

    if choice != "y":
        print("Thank you for using the Safe Calculator!")
        break
