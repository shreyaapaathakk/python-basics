"""
Nested Loops

This script demonstrates nested loops.
"""

for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row}, {column})", end=" ")

    print()

print("\nStar Pattern")

for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")

    print()
