"""
Looping Through Lists

This script demonstrates different ways to iterate through lists.
"""

fruits = ["Apple", "Banana", "Orange", "Mango"]

print("Using for loop")

for fruit in fruits:
    print(fruit)

print("\nUsing index")

for index in range(len(fruits)):
    print(index, fruits[index])

print("\nUsing enumerate")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
