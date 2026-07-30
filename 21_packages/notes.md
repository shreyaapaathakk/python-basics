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

---

# Absolute Imports

An absolute import starts from the project's top-level package.

Example:

```python
from my_package.calculator import add

print(add(5, 3))
```

Advantages:

- Easy to understand
- Explicit
- Preferred in large projects

---

# Relative Imports

A relative import refers to another module inside the same package.

Example:

```python
from .calculator import add
```

The single dot (`.`) refers to the current package.

Two dots (`..`) refer to the parent package.

Example:

```python
from ..utilities import helper
```

---

# Absolute vs Relative Imports

| Absolute Import | Relative Import |
|-----------------|-----------------|
|Starts from the top-level package|Starts from the current package|
|Easy to read|Shorter within packages|
|Works from project entry points|Works only inside packages|
|Preferred for application code|Useful for package internals|

---

# Common Mistake

If you run a package module directly:

```bash
python greetings.py
```

a relative import like:

```python
from .calculator import add
```

may produce:

```
ImportError:
attempted relative import with no known parent package
```

Instead, run the package from the project root:

```bash
python -m my_package.greetings
```

or import the package from another script.

---

# Best Practices

- Use **absolute imports** in application entry-point scripts.
- Use **relative imports** for modules within the same package.
- Avoid mixing import styles unnecessarily.
- Keep package structures simple and well organized.
