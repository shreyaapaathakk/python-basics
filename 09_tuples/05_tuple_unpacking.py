"""
Tuple Unpacking

This script demonstrates tuple unpacking.
"""

student = ("Alice", 22, "Computer Science")

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)

# Using *
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)
