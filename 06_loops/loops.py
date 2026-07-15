"""
Python Loops

This script demonstrates for and while loops in Python.
"""

print("=== For Loop ===")

# Example 1: Print numbers from 1 to 5
for number in range(1, 6):
    print(number)


print("\n=== Iterating Over a String ===")

for letter in "Python":
    print(letter)


print("\n=== Iterating Over a List ===")

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


print("\n=== While Loop ===")

count = 1

while count <= 5:
    print(count)
    count += 1


print("\n=== Break Statement ===")

for number in range(1, 11):
    if number == 6:
        break
    print(number)


print("\n=== Continue Statement ===")

for number in range(1, 6):
    if number == 3:
        continue
    print(number)


print("\n=== Else with a Loop ===")

for number in range(1, 4):
    print(number)
else:
    print("Loop completed successfully.")
