"""
03_filter.py

Using filter() to select data.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = filter(lambda number: number % 2 == 0, numbers)

print(list(even_numbers))
