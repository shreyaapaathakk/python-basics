# Decorators

## Introduction

A decorator is a function that takes another function as input, adds extra functionality, and returns a new function.

Instead of modifying the original function, decorators wrap it with additional behavior.

---

# Why Decorators?

Without decorators:

```python
print("Start")
greet()
print("End")
```

With decorators:

```python
@decorator
def greet():
```

Cleaner and reusable.

---

# Functions are Objects

Functions can be:

- Assigned to variables
- Passed as arguments
- Returned from functions

Example:

```python
def hello():
    print("Hello")

greet = hello
greet()
```

---

# Nested Functions

Functions can exist inside other functions.

Example:

```python
def outer():

    def inner():
        print("Hi")
```

---

# Basic Decorator

A decorator usually has this structure:

```python
def decorator(function):

    def wrapper():
        function()

    return wrapper
```

Usage:

```python
@decorator
def greet():
```

---

# How It Works

When Python sees:

```python
@decorator
def greet():
```

It becomes:

```python
greet = decorator(greet)
```

---

# Decorators with Parameters

If the decorated function accepts arguments:

```python
def wrapper(name):
```

For more flexibility:

```python
def wrapper(*args, **kwargs):
```

---

# Multiple Decorators

Example:

```python
@A
@B
def function():
```

Execution order:

```
A(
    B(
        function
    )
)
```

---

# Real-World Uses

- Logging
- Authentication
- Timing
- Validation
- Memoization
- Debugging

---

# Best Practices

- Keep decorators focused on one task.
- Use meaningful names.
- Prefer `*args` and `**kwargs` for reusable decorators.
- Preserve function metadata using `functools.wraps` in production code.

---

# Summary

Decorators:

- Wrap functions
- Reuse code
- Improve readability
- Separate concerns
- Are widely used in Python frameworks like Flask and Django
