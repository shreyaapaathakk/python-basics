"""
Modifying Lists

This script demonstrates how to modify list elements.
"""

fruits = ["Apple", "Banana", "Orange"]

print("Original List:", fruits)

# Modify an item
fruits[1] = "Mango"

print("After Modification:", fruits)

# Add a new item
fruits.append("Grapes")

print("After Append:", fruits)

# Insert an item
fruits.insert(1, "Kiwi")

print("After Insert:", fruits)

# Remove an item
fruits.remove("Orange")

print("After Remove:", fruits)

# Remove last item
fruits.pop()

print("After Pop:", fruits)
