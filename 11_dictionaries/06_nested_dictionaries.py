"""
Nested Dictionaries

This script demonstrates dictionaries inside dictionaries.
"""

students = {
    "student1": {
        "name": "Alice",
        "marks": 90
    },
    "student2": {
        "name": "Bob",
        "marks": 85
    },
    "student3": {
        "name": "Charlie",
        "marks": 95
    }
}

print("Student Records\n")

for student_id, details in students.items():
    print(student_id)
    print("Name :", details["name"])
    print("Marks:", details["marks"])
    print()
