"""
practice.py

Solutions for iterator and generator exercises.
"""

print("=" * 10, "Exercise 1", "=" * 10)

fruits = ("Apple", "Banana", "Cherry")
iterator = iter(fruits)

print(next(iterator))
print(next(iterator))
print(next(iterator))


print("\n" + "=" * 10, "Exercise 2", "=" * 10)

numbers = iter([1, 2, 3])

for number in numbers:
    print(number)


print("\n" + "=" * 10, "Exercise 3", "=" * 10)

letters = iter("ABC")

try:
    while True:
        print(next(letters))
except StopIteration:
    print("Iterator finished.")


print("\n" + "=" * 10, "Exercise 4", "=" * 10)


class Counter:
    """Custom iterator that counts from a start value to an end value."""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


for number in Counter(10, 20):
    print(number)


print("\n" + "=" * 10, "Exercise 5", "=" * 10)


def even_numbers(limit):
    """Yield even numbers up to a given limit."""
    for number in range(2, limit + 1, 2):
        yield number


for number in even_numbers(20):
    print(number)


print("\n" + "=" * 10, "Exercise 6", "=" * 10)

cubes = (number ** 3 for number in range(1, 11))

for cube in cubes:
    print(cube)


print("\n" + "=" * 10, "Exercise 7", "=" * 10)


def characters(text):
    """Yield one character at a time from a string."""
    for character in text:
        yield character


for character in characters("Python"):
    print(character)


print("\n" + "=" * 10, "Bonus Challenge", "=" * 10)


def fibonacci(limit):
    """Yield Fibonacci numbers up to a specified count."""
    first, second = 0, 1
    count = 0

    while count < limit:
        yield first
        first, second = second, first + second
        count += 1


for number in fibonacci(10):
    print(number)
