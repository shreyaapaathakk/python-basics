"""
01_iterators.py

Understanding Python iterators.
"""

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Uncommenting the next line raises StopIteration
# print(next(iterator))
