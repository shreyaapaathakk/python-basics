"""
Method Overriding

This script demonstrates overriding inherited methods.
"""


class Animal:
    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("Dog barks.")


animal = Animal()
dog = Dog()

animal.speak()
dog.speak()
