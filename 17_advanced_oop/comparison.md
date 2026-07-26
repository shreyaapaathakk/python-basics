# Advanced OOP Comparison Guide

This guide summarizes the key concepts introduced in the Advanced OOP module.

---

# Instance Variables vs Class Variables

| Instance Variable | Class Variable |
|-------------------|----------------|
| Belongs to an object | Belongs to the class |
| Each object has its own copy | Shared by all objects |
| Defined using `self` | Defined inside the class |
| Changes affect one object | Changes affect every object |

Example:

```python
class Student:

    school = "ABC School"      # Class variable

    def __init__(self, name):
        self.name = name       # Instance variable
```

---

# Instance Method vs Class Method vs Static Method

| Instance Method | Class Method | Static Method |
|-----------------|--------------|---------------|
| Uses `self` | Uses `cls` | Uses neither |
| Access object data | Access class data | Utility function |
| Called by an object | Called by class or object | Called by class or object |

Example:

```python
class Example:

    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass
```

---

# self vs cls

| self | cls |
|------|------|
| Refers to an object | Refers to the class |
| Used in instance methods | Used in class methods |
| Accesses object variables | Accesses class variables |

---

# Getter vs Setter

| Getter | Setter |
|---------|---------|
| Reads a value | Updates a value |
| Uses `@property` | Uses `@property_name.setter` |
| Performs safe access | Performs validation before assignment |

Example:

```python
@property
def age(self):
    return self._age
```

```python
@age.setter
def age(self, value):
    self._age = value
```

---

# __str__() vs __repr__()

| __str__() | __repr__() |
|------------|------------|
| Human-readable | Developer-friendly |
| Used by `print()` | Used by `repr()` |
| Easy to understand | Useful for debugging |

---

# Method Overloading vs Method Overriding

| Method Overloading | Method Overriding |
|--------------------|-------------------|
| Not directly supported in Python | Fully supported |
| Same method name with different parameters (simulated using default arguments or `*args`) | Child class replaces parent method |
| Happens in the same class | Happens across inheritance |

---

# Inheritance vs Multiple Inheritance

| Inheritance | Multiple Inheritance |
|-------------|----------------------|
| One parent class | More than one parent class |
| Easier to understand | More flexible |
| Less complex | Can increase complexity |

---

# Encapsulation vs Abstraction

| Encapsulation | Abstraction |
|---------------|-------------|
| Protects data | Hides implementation |
| Uses private attributes | Uses abstract classes |
| Controls access | Defines required behavior |

---

# Method Overriding vs super()

| Method Overriding | super() |
|-------------------|---------|
| Replaces parent behavior | Reuses parent behavior |
| Child provides new implementation | Child extends parent implementation |

Example:

```python
class Dog(Animal):

    def __init__(self):
        super().__init__()
```

---

# Common Magic Methods

| Method | Purpose |
|---------|---------|
| `__init__()` | Constructor |
| `__str__()` | String representation |
| `__repr__()` | Official representation |
| `__len__()` | Object length |
| `__eq__()` | Equality comparison |
| `__add__()` | Addition |
| `__sub__()` | Subtraction |
| `__mul__()` | Multiplication |
| `__lt__()` | Less than |
| `__gt__()` | Greater than |

---

# Operator vs Magic Method

| Operator | Magic Method |
|-----------|--------------|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `==` | `__eq__()` |
| `<` | `__lt__()` |
| `>` | `__gt__()` |

---

# Basic OOP vs Advanced OOP

| Basic OOP | Advanced OOP |
|------------|--------------|
| Classes | Class Methods |
| Objects | Static Methods |
| Constructors | Properties |
| Inheritance | Multiple Inheritance |
| Encapsulation | Magic Methods |
| Abstraction | Operator Overloading |
| Polymorphism | Method Resolution Order (MRO) |
| Methods | `super()` |

---

# When Should You Use Each?

| Feature | Best Used For |
|---------|---------------|
| Class Variable | Shared data |
| Instance Variable | Object-specific data |
| Class Method | Working with class-level data |
| Static Method | Utility/helper functions |
| Property | Controlled access to attributes |
| Magic Method | Customizing built-in behavior |
| Inheritance | Reusing existing code |
| Multiple Inheritance | Combining behaviors from multiple classes |
| Method Overriding | Customizing inherited behavior |
| `super()` | Reusing parent class functionality |
| Operator Overloading | Making custom objects behave like built-in types |

---

# Quick Revision Checklist

Before moving to the next module, make sure you can:

- ✅ Create classes and objects
- ✅ Differentiate class and instance variables
- ✅ Write instance, class, and static methods
- ✅ Use property decorators
- ✅ Override methods
- ✅ Use `super()`
- ✅ Create and use multiple inheritance
- ✅ Implement common magic methods
- ✅ Overload operators
- ✅ Choose the right OOP feature for the right situation

Congratulations! You have completed the Advanced OOP module and are ready to explore more advanced Python topics such as Iterators & Generators.
