"""
Common Set Methods

This script demonstrates useful set methods.
"""

numbers = {10, 20, 30}

print("Original:", numbers)

numbers.add(40)
print("After add():", numbers)

numbers.update([50, 60])
print("After update():", numbers)

numbers.discard(20)
print("After discard():", numbers)

copy_set = numbers.copy()

print("Copied Set:", copy_set)

numbers.clear()

print("After clear():", numbers)
