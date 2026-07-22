"""
Frozen Sets

This script demonstrates immutable sets.
"""

numbers = frozenset([1, 2, 3, 4, 5])

print("Frozen Set:", numbers)

print("Length:", len(numbers))

print("Is 3 present?", 3 in numbers)

# The following would raise an error:
# numbers.add(6)
