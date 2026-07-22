"""
Tuple Operations

This script demonstrates common tuple operations.
"""

numbers = (10, 20, 30)

print("Original Tuple:", numbers)

# Concatenation
new_numbers = numbers + (40, 50)

print("After Concatenation:", new_numbers)

# Repetition
print("Repeated Tuple:", numbers * 2)

# Membership
print("Is 20 present?", 20 in numbers)

print("Length:", len(numbers))
