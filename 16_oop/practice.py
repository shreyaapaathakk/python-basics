"""
Practice Solutions - Object-Oriented Programming
"""

print("=" * 10, "Exercise 1", "=" * 10)


class Car:
    pass


print("=" * 10, "Exercise 2", "=" * 10)

car1 = Car()
car2 = Car()

print(type(car1))
print(type(car2))

print("=" * 10, "Exercise 3", "=" * 10)


class Person:
    def __init__(self, name):
        self.name = name


person = Person("Alice")
print(person.name)

print("=" * 10, "Exercise 4", "=" * 10)


class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello! My name is {self.name}.")


Student("Bob").introduce()

print("=" * 10, "Exercise 5", "=" * 10)


class Animal:
    pass


class Dog(Animal):
    pass


print(Dog())

print("=" * 10, "Exercise 6", "=" * 10)


class Cat:
    def speak(self):
        print("Meow!")


class Bird:
    def speak(self):
        print("Chirp!")


for animal in [Cat(), Bird()]:
    animal.speak()

print("=" * 10, "Exercise 7", "=" * 10)


class Account:
    def __init__(self):
        self.__balance = 500

    def get_balance(self):
        return self.__balance


print(Account().get_balance())

print("=" * 10, "Exercise 8", "=" * 10)

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class CarVehicle(Vehicle):
    def start(self):
        print("Car started.")


CarVehicle().start()

print("=" * 10, "Bonus Challenge", "=" * 10)

print("See challenge.py for the complete Library Management System.")
