"""
05_sorting_with_lambda.py

Sorting using lambda functions.
"""

students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 95),
    ("David", 81)
]

students.sort(key=lambda student: student[1])

print(students)
