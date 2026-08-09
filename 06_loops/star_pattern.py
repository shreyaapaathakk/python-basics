"""
Star Patterns

This script demonstrates how nested loops
can be used to create different patterns.
"""

print("===== Right Triangle =====")

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")

    print()


print("\n===== Inverted Triangle =====")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")

    print()


print("\n===== Pyramid =====")

for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "* " * i

    print(spaces + stars)
