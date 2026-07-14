"""
Python Conditional Statements

This script demonstrates how to use if, elif, and else statements.
"""

# Example 1: Simple if statement
age = 20

print("=== Example 1 ===")
if age >= 18:
    print("You are eligible to vote.")


# Example 2: if-else statement
number = 7

print("\n=== Example 2 ===")
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# Example 3: if-elif-else statement
marks = 85

print("\n=== Example 3 ===")
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Grade: {grade}")


# Example 4: Nested if statement
is_student = True
age = 20

print("\n=== Example 4 ===")
if is_student:
    if age < 25:
        print("Eligible for student discount.")
    else:
        print("Student discount not available.")
else:
    print("Not a student.")
