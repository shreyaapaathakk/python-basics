"""
Python Input and Output

This script demonstrates how to take user input
and display output using the print() function.
"""

# Output
print("=== Welcome to Python Input & Output ===")

# Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in feet): "))

print("\n=== User Details ===")
print("Name:", name)
print("Age:", age)
print("Height:", height)

# Using f-strings
print(f"\nHello, {name}! You are {age} years old and {height} feet tall.")
