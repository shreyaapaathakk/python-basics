# Advanced Object-Oriented Programming (Advanced OOP)

## Introduction

In the previous OOP module, you learned about:

- Classes
- Objects
- Constructors
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

This module introduces more advanced features that make Python classes more powerful, reusable, and easier to maintain.

---

# Class Variables vs Instance Variables

## Instance Variables

Instance variables belong to each object.

Each object has its own copy.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

```python
student1 = Student("Alice")
student2 = Student("Bob")
```

Each student has a different `name`.

---

## Class Variables

Class variables are shared among all objects.

Example:

```python
class Student:

    school = "ABC School"
```

Every object uses the same value.

```python
print(Student.school)
```

Use class variables for information common to every object.

Examples:

- Company name
- School name
- Tax rate
- Country

---

# Class Methods

Class methods work with class variables.

Decorator:

```python
@classmethod
```

Syntax:

```python
class Student:

    school = "ABC"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name
```

Notice that the first parameter is:

```python
cls
```

instead of

```python
self
```

---

## When to Use Class Methods

Use them when you need to:

- Change class variables
- Create alternative constructors
- Perform operations related to the class instead of a specific object

---

# Static Methods

Static methods belong to the class but do not access:

- instance variables
- class variables

Decorator:

```python
@staticmethod
```

Example:

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
```

Call using

```python
Calculator.add(5, 3)
```

---

## When to Use Static Methods

Use static methods for utility functions.

Examples:

- Math calculations
- Unit conversions
- Validation functions
- Helper methods

---

# Property Decorators

Properties allow you to control how attributes are accessed.

Instead of calling methods like

```python
temperature.get_temperature()
```

you can simply write

```python
temperature.celsius
```

---

## Getter

```python
@property

def celsius(self):
    return self._celsius
```

---

## Setter

```python
@celsius.setter

def celsius(self, value):
    self._celsius = value
```

The setter lets you validate data before assigning it.

Example:

```python
if value < -273.15:
    raise ValueError()
```

---

## Deleter

Properties can also define a deleter.

```python
@celsius.deleter

def celsius(self):
    del self._celsius
```

Deleters are less common but can be useful when cleaning up object state.

---

# Magic (Dunder) Methods

Magic methods begin and end with double underscores.

Examples:

```
__init__
__str__
__repr__
__len__
__eq__
__add__
```

Python automatically calls these methods.

---

## __init__()

Runs automatically when an object is created.

```python
person = Person()
```

---

## __str__()

Controls how an object is displayed.

Example:

```python
print(book)
```

instead of

```
<__main__.Book object at ...>
```

---

## __repr__()

Returns an official string representation of an object.

Mostly used for debugging.

Example:

```python
repr(book)
```

---

## __len__()

Defines how

```python
len(object)
```

works.

Example:

```python
class Book:

    def __len__(self):
        return len(self.title)
```

---

## __eq__()

Defines equality.

Example:

```python
book1 == book2
```

---

# Multiple Inheritance

A class can inherit from more than one parent class.

Example:

```python
class Flyer:

    pass


class Swimmer:

    pass


class Duck(Flyer, Swimmer):

    pass
```

Duck receives features from both parents.

---

# Method Resolution Order (MRO)

When multiple inheritance is used, Python must decide where to look first.

Example:

```python
class A:

    pass


class B(A):

    pass


class C(A):

    pass


class D(B, C):

    pass
```

Python follows the MRO.

Check it using

```python
print(D.mro())
```

---

# Method Overriding

A child class can replace a parent's method.

Parent:

```python
class Animal:

    def speak(self):
        print("Animal")
```

Child:

```python
class Dog(Animal):

    def speak(self):
        print("Woof!")
```

---

# super()

`super()` allows a child class to use code from its parent.

Example:

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):

        super().__init__(name)

        self.breed = breed
```

Benefits:

- Avoids duplicate code
- Improves readability
- Makes inheritance easier to maintain

---

# Operator Overloading

Python operators can work with your own classes.

Example:

```python
point1 + point2
```

Python internally calls

```python
__add__()
```

Other common operators:

| Operator | Magic Method |
|-----------|--------------|
| + | __add__ |
| - | __sub__ |
| * | __mul__ |
| / | __truediv__ |
| == | __eq__ |
| < | __lt__ |
| > | __gt__ |

---

# Best Practices

✅ Use instance variables for object-specific data.

✅ Use class variables for shared data.

✅ Use class methods to work with class variables.

✅ Use static methods for utility functions.

✅ Validate important data using properties.

✅ Override methods only when necessary.

✅ Use `super()` instead of rewriting parent code.

✅ Keep classes small and focused on one responsibility.

✅ Write meaningful docstrings for every class and method.

✅ Follow PEP 8 naming conventions.

---

# Summary

In this module, you learned about:

- Class variables
- Instance variables
- Class methods
- Static methods
- Properties
- Getters and setters
- Magic methods
- Multiple inheritance
- Method Resolution Order (MRO)
- Method overriding
- `super()`
- Operator overloading

These concepts are commonly used in professional Python applications and will help you write cleaner, more reusable, and maintainable object-oriented code.
