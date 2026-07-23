"""
Looping Through Dictionaries

This script demonstrates different ways to iterate through dictionaries.
"""

student = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science"
}

print("Keys")

for key in student:
    print(key)

print("\nValues")

for value in student.values():
    print(value)

print("\nKey-Value Pairs")

for key, value in student.items():
    print(f"{key}: {value}")
