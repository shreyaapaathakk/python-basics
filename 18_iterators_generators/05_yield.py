"""
05_yield.py

Understanding the yield keyword.
"""


def greetings():
    yield "Hello"
    yield "Welcome"
    yield "Goodbye"


generator = greetings()

print(next(generator))
print(next(generator))
print(next(generator))
