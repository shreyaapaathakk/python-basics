"""
02_custom_iterator.py

Creating a custom iterator.
"""


class CountUp:
    """Iterator that counts from 1 to a limit."""

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        number = self.current
        self.current += 1
        return number


counter = CountUp(5)

for number in counter:
    print(number)
