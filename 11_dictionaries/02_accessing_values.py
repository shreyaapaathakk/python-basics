"""
Accessing Dictionary Values

This script demonstrates how to access values in a dictionary.
"""

student = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science"
}

print("Name:", student["name"])
print("Age:", student["age"])

# Using get()
print("Course:", student.get("course"))

# Key that does not exist
print("City:", student.get("city", "Not Available"))
