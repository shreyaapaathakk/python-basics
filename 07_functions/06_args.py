"""
Variable-Length Positional Arguments
"""


def total(*numbers):
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))


total(10, 20)
total(5, 10, 15, 20)
