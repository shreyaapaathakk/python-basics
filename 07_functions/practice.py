"""
Practice Exercises
"""

# Exercise 1
# Write a function to find the square of a number.


def square(number):
    return number * number


print("Square:", square(6))


# Exercise 2
# Write a function to determine whether a number is even.


def is_even(number):
    return number % 2 == 0


print("Is 8 even?", is_even(8))


# Exercise 3
# Write a function to find the largest of two numbers.


def maximum(a, b):
    return max(a, b)


print("Largest:", maximum(10, 15))


# Exercise 4
# Write a function that greets a user.


def greet(name):
    print(f"Welcome, {name}!")


greet("Python Learner")


# Exercise 5
# Write a function that calculates the area of a rectangle.


def area(length, width):
    return length * width


print("Area:", area(5, 4))
