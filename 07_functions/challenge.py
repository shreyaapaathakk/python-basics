"""
Challenge: Simple Calculator

Create a calculator function that takes two numbers
and an operator (+, -, *, /) as input
and returns the result.
"""


def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        return "Cannot divide by zero."
    else:
        return "Invalid operator."


num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

print("Result:", calculator(num1, num2, operator))
