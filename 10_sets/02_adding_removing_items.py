"""
Adding and Removing Items

This script demonstrates how to modify sets.
"""

fruits = {"Apple", "Banana", "Orange"}

print("Original Set:", fruits)

# Add an item
fruits.add("Mango")

print("After add():", fruits)

# Add multiple items
fruits.update(["Grapes", "Kiwi"])

print("After update():", fruits)

# Remove an item
fruits.remove("Banana")

print("After remove():", fruits)

# Discard an item
fruits.discard("Pineapple")

print("After discard():", fruits)

# Remove a random item
removed_item = fruits.pop()

print("Removed:", removed_item)
print("Current Set:", fruits)
