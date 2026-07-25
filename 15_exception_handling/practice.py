"""
Practice Solutions - Exception Handling
"""

print("=" * 10, "Exercise 1", "=" * 10)

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid number.")

print("=" * 10, "Exercise 2", "=" * 10)

try:
    result = 100 / int(input("Enter a divisor: "))
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

print("=" * 10, "Exercise 3", "=" * 10)

try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

print("=" * 10, "Exercise 4", "=" * 10)

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)

print("=" * 10, "Exercise 5", "=" * 10)

try:
    print("Program running.")

finally:
    print("Program finished.")

print("=" * 10, "Exercise 6", "=" * 10)


def check_number(number):
    if number < 0:
        raise ValueError("Negative number.")

    return number


try:
    print(check_number(int(input("Enter a number: "))))

except ValueError as error:
    print(error)

print("=" * 10, "Exercise 7", "=" * 10)


class InvalidAgeError(Exception):
    """Custom exception."""


try:
    age = int(input("Enter age: "))

    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

    print("Access granted.")

except InvalidAgeError as error:
    print(error)

print("=" * 10, "Exercise 8", "=" * 10)

try:
    with open("sample.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")

print("=" * 10, "Bonus Challenge", "=" * 10)

print("See challenge.py")
