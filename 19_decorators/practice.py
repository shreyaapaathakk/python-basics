"""
practice.py

Solutions for decorator exercises.
"""

print("=" * 10, "Exercise 1", "=" * 10)


def greet():
    """Print a greeting."""
    print("Hello!")


hello = greet
hello()


print("\n" + "=" * 10, "Exercise 2", "=" * 10)


def outer():
    """Demonstrate a nested function."""

    def inner():
        print("Inside the inner function.")

    inner()


outer()


print("\n" + "=" * 10, "Exercise 3", "=" * 10)


def before_decorator(function):
    """Print a message before calling the function."""

    def wrapper():
        print("Before execution")
        function()

    return wrapper


@before_decorator
def say_hi():
    print("Hi!")


say_hi()


print("\n" + "=" * 10, "Exercise 4", "=" * 10)


def around_decorator(function):
    """Print messages before and after calling the function."""

    def wrapper():
        print("Start")
        function()
        print("End")

    return wrapper


@around_decorator
def welcome():
    print("Welcome!")


welcome()


print("\n" + "=" * 10, "Exercise 5", "=" * 10)


def name_decorator(function):
    """Decorate a function that accepts one argument."""

    def wrapper(name):
        print("Greeting user...")
        function(name)

    return wrapper


@name_decorator
def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Alice")


print("\n" + "=" * 10, "Exercise 6", "=" * 10)


def stars(function):
    def wrapper():
        print("*" * 20)
        function()
        print("*" * 20)

    return wrapper


def heading(function):
    def wrapper():
        print("Decorators Demo")
        function()

    return wrapper


@stars
@heading
def demo():
    print("Multiple decorators in action.")


demo()


print("\n" + "=" * 10, "Exercise 7", "=" * 10)


def logger(function):
    """Decorator using *args and **kwargs."""

    def wrapper(*args, **kwargs):
        print("Calling function...")
        return function(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    return a + b


print(add(5, 7))


print("\n" + "=" * 10, "Bonus Challenge", "=" * 10)

import time


def timer(function):
    """Measure execution time."""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result

    return wrapper


@timer
def slow_task():
    total = 0
    for number in range(1_000_000):
        total += number
    return total


slow_task()
