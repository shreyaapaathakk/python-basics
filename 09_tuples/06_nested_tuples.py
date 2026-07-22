"""
Nested Tuples

This script demonstrates tuples inside tuples.
"""

students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
)

print("Student Records\n")

for student in students:
    print("Name :", student[0])
    print("Marks:", student[1])
    print()
