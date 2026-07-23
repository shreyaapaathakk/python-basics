"""
Adding and Updating Dictionary Items

This script demonstrates how to add, update, and remove items.
"""

student = {
    "name": "Alice",
    "age": 22
}

print("Original Dictionary:", student)

# Add a new key-value pair
student["course"] = "Computer Science"

print("After Adding:", student)

# Update an existing value
student["age"] = 23

print("After Updating:", student)

# Remove an item
student.pop("course")

print("After pop():", student)

# Add another item
student["city"] = "Delhi"

print("Final Dictionary:", student)
