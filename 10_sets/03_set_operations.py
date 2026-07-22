"""
Set Operations

This script demonstrates common mathematical operations on sets.
"""

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection:", set_a & set_b)

# Difference
print("Difference (A - B):", set_a - set_b)

# Symmetric Difference
print("Symmetric Difference:", set_a ^ set_b)
