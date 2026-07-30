# Python Packages

## Introduction

A package is a directory that contains one or more Python modules.

Packages help organize related code into logical groups.

---

# Module vs Package

| Module | Package |
|---------|----------|
|Single `.py` file|Directory of modules|
|Small programs|Large applications|
|Contains functions/classes|Contains multiple modules|

---

# Package Structure

Example:

```text
my_package/
│
├── __init__.py
├── calculator.py
├── greetings.py
└── utilities.py
```

---

# `__init__.py`

The `__init__.py` file tells Python that a directory should be treated as a package.

It can also expose selected functions for easier imports.

Example:

```python
from .calculator import add
```

---

# Importing Modules

Import an entire module:

```python
from my_package import calculator

print(calculator.add(2, 3))
```

Import a specific function:

```python
from my_package.calculator import add

print(add(2, 3))
```

---

# Import Aliases

Use shorter names with the `as` keyword.

Example:

```python
import my_package.calculator as calc

print(calc.multiply(4, 5))
```

---

# Benefits of Packages

- Better organization
- Code reuse
- Easier maintenance
- Clear project structure
- Scalable applications

---

# Best Practices

- Use meaningful package names.
- Keep related modules together.
- Write docstrings for modules.
- Avoid circular imports.
- Export only necessary functions in `__init__.py`.

---

# Summary

- A package is a collection of related modules.
- `__init__.py` identifies a package.
- Packages improve organization and scalability.
- Imports can target modules or individual functions.
