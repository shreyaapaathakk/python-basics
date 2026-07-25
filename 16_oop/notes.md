# Object-Oriented Programming (OOP)

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes programs into **objects**.

An object contains:

- Attributes (data)
- Methods (functions)

Example:

```python
class Student:
    pass
```

---

## Four Pillars of OOP

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

---

## Class

A class is a blueprint for creating objects.

```python
class Car:
    pass
```

---

## Object

An object is an instance of a class.

```python
car = Car()
```

---

## Constructor

```python
def __init__(self):
```

Runs automatically when an object is created.

---

## self

`self` refers to the current object.

---

## Methods

Methods define an object's behavior.

```python
def greet(self):
    print("Hello")
```

---

## Inheritance

Allows one class to inherit features from another.

```python
class Dog(Animal):
```

---

## Polymorphism

Different classes can provide their own implementation of the same method.

---

## Encapsulation

Protects object data using private attributes.

```python
self.__balance
```

---

## Abstraction

Hides implementation details and exposes only essential functionality.

---

## Benefits of OOP

- Reusable code
- Easier maintenance
- Better organization
- Scalable applications
- Cleaner design

---

## Best Practices

- Use meaningful class names.
- Keep methods focused on one task.
- Use private attributes when appropriate.
- Favor composition where it makes sense.
- Write docstrings for classes and methods.
