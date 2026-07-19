"""
Challenge: Number Checker

Write a program that:

1. Takes two numbers from the user.
2. Displays:
   - Sum
   - Difference
   - Product
   - Quotient
3. Compares the two numbers.
4. Checks if both numbers are positive.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n===== Arithmetic Operations =====")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")

print("\n===== Comparison =====")
print("Equal:", num1 == num2)
print("Greater Than:", num1 > num2)
print("Less Than:", num1 < num2)

print("\n===== Logical =====")
print("Both Positive:", num1 > 0 and num2 > 0)
