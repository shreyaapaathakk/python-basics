"""
Common Dictionary Methods

This script demonstrates useful dictionary methods.
"""

student = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science"
}

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

copy_student = student.copy()

print("Copied Dictionary:", copy_student)

student.clear()

print("After clear():", student)
