"""
Nested Lists

This script demonstrates lists inside lists.
"""

students = [
    ["Alice", 90],
    ["Bob", 85],
    ["Charlie", 95]
]

print("Student Records")

for student in students:
    print("Name:", student[0])
    print("Marks:", student[1])
    print()
