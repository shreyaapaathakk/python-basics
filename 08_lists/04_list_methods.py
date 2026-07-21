"""
Common List Methods

This script demonstrates frequently used list methods.
"""

numbers = [5, 2, 9, 1, 7]

print("Original:", numbers)

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

numbers.append(100)
print("Append:", numbers)

numbers.extend([200, 300])
print("Extend:", numbers)

print("Count of 100:", numbers.count(100))

print("Index of 9:", numbers.index(9))

numbers.clear()

print("After Clear:", numbers)
