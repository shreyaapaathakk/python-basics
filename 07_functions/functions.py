"""
Python Functions

This script demonstrates how to define and use functions in Python.
"""

print("=== Function Without Parameters ===")


def greet():
    print("Hello! Welcome to Python.")


greet()


print("\n=== Function With Parameters ===")


def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")


greet_user("Shreya")


print("\n=== Function That Returns a Value ===")


def add(a, b):
    return a + b


result = add(10, 5)
print("Sum:", result)


print("\n=== Default Parameters ===")


def introduce(name, country="India"):
    print(f"My name is {name}. I live in {country}.")


introduce("Shreya")
introduce("Alice", "Canada")


print("\n=== Keyword Arguments ===")


def student(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")


student(age=22, name="Shreya")


print("\n=== Variable-Length Arguments (*args) ===")


def total(*numbers):
    print("Sum:", sum(numbers))


total(10, 20)
total(5, 10, 15, 20)


print("\n=== Variable-Length Keyword Arguments (**kwargs) ===")


def profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


profile(name="Shreya", age=22, language="Python")
