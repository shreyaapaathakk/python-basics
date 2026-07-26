"""
Practice Solutions - Advanced OOP
"""

print("=" * 10, "Exercise 1", "=" * 10)


class Company:
    """Represents a company."""

    company_name = "Tech Solutions"

    @classmethod
    def change_company_name(cls, new_name):
        """Change the company name."""
        cls.company_name = new_name


print("Before:", Company.company_name)

Company.change_company_name("Innovate Tech")

print("After:", Company.company_name)


print("\n" + "=" * 10, "Exercise 2", "=" * 10)


class Calculator:
    """Provides utility methods."""

    @staticmethod
    def square(number):
        """Return the square of a number."""
        return number ** 2


print("Square of 8:", Calculator.square(8))


print("\n" + "=" * 10, "Exercise 3", "=" * 10)


class Temperature:
    """Represents temperature in Celsius."""

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Return the temperature."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Validate and set the temperature."""
        if value < -273.15:
            raise ValueError(
                "Temperature cannot be below absolute zero."
            )

        self._celsius = value


temperature = Temperature(25)

print("Current:", temperature.celsius)

temperature.celsius = 30

print("Updated:", temperature.celsius)


print("\n" + "=" * 10, "Exercise 4", "=" * 10)


class Book:
    """Represents a book."""

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"


book = Book("Python Basics")

print(book)


print("\n" + "=" * 10, "Exercise 5", "=" * 10)


class Flyer:
    """Represents flying behavior."""

    def fly(self):
        print("Flying...")


class Swimmer:
    """Represents swimming behavior."""

    def swim(self):
        print("Swimming...")


class Duck(Flyer, Swimmer):
    """Duck inherits from Flyer and Swimmer."""


duck = Duck()

duck.fly()
duck.swim()


print("\n" + "=" * 10, "Exercise 6", "=" * 10)


class Animal:
    """Base class."""

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):
    """Derived class."""

    def speak(self):
        print("Dog barks.")


animal = Animal()
dog = Dog()

animal.speak()
dog.speak()


print("\n" + "=" * 10, "Exercise 7", "=" * 10)


class Vehicle:
    """Base class."""

    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    """Derived class."""

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


car = Car("Toyota", "Corolla")

print("Brand:", car.brand)
print("Model:", car.model)


print("\n" + "=" * 10, "Exercise 8", "=" * 10)


class Point:
    """Represents a point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __str__(self):
        return f"({self.x}, {self.y})"


point1 = Point(2, 4)
point2 = Point(5, 6)

print(point1 + point2)


print("\n" + "=" * 10, "Bonus Challenge", "=" * 10)


class BankAccount:
    """Represents a bank account."""

    bank_name = "Python Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        """Return account balance."""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Validate balance."""
        if amount < 0:
            raise ValueError(
                "Balance cannot be negative."
            )

        self._balance = amount

    @classmethod
    def bank(cls):
        """Display bank name."""
        print(cls.bank_name)

    @staticmethod
    def minimum_balance():
        """Return minimum required balance."""
        return 100

    def __add__(self, other):
        return self.balance + other.balance

    def __str__(self):
        return (
            f"{self.owner}: ${self.balance}"
        )


account1 = BankAccount("Alice", 1200)
account2 = BankAccount("Bob", 800)

print(account1)
print(account2)

print("Combined Balance:", account1 + account2)

BankAccount.bank()

print(
    "Minimum Balance:",
    BankAccount.minimum_balance()
)
