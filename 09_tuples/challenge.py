"""
Mini Project: Student Record Viewer

Concepts Used:
- Tuples
- Tuple unpacking
- Loops
- Conditionals
"""

students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95),
    ("David", 88)
)

print("===== Student Record Viewer =====")

search_name = input("Enter student name: ").title()

found = False

for name, marks in students:
    if name == search_name:
        print("\nStudent Found")
        print("Name :", name)
        print("Marks:", marks)
        found = True
        break

if not found:
    print("\nStudent record not found.")
