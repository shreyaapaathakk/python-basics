"""
02_map.py

Using map() to transform data.
"""

numbers = [1, 2, 3, 4, 5]

squares = map(lambda number: number ** 2, numbers)

print(list(squares))
