"""
Inheritance

This script demonstrates inheritance.
"""


class Animal:
    """Base class."""

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):
    """Derived class."""

    def bark(self):
        print("Dog barks.")


dog = Dog()

dog.speak()
dog.bark()
