"""
Fibonacci Sequence

The Fibonacci sequence is a sequence where
each number is the sum of the two previous numbers.

Example:
0, 1, 1, 2, 3, 5, 8, 13...
"""

terms = int(input("How many Fibonacci terms do you want? "))

first = 0
second = 1

print("\nFibonacci Sequence:")

for _ in range(terms):
    print(first, end=" ")

    next_term = first + second
    first = second
    second = next_term

print()
