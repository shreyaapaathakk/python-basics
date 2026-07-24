# Python Modules

## What is a Module?

A module is a Python file that contains functions, variables, or classes that can be reused in other programs.

Example:

```python
import math
```

---

## Why Use Modules?

- Reuse code
- Organize programs
- Reduce repetition
- Make projects easier to maintain

---

## Importing a Module

```python
import math

print(math.sqrt(16))
```

---

## Importing with an Alias

```python
import math as m

print(m.pi)
```

Aliases make code shorter and easier to read.

---

## Importing Specific Items

```python
from math import sqrt

print(sqrt(25))
```

Multiple items

```python
from random import randint, choice
```

---

## Built-in Modules

Some commonly used modules:

| Module | Purpose |
|---------|----------|
| math | Mathematical functions |
| random | Random values |
| datetime | Date and time |
| os | Operating system functions |
| statistics | Statistical calculations |

---

## Creating a Custom Module

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

Using it:

```python
import calculator

print(calculator.add(2, 3))
```

---

## The __name__ Variable

Every Python file has a special variable called `__name__`.

When a file is run directly:

```python
__name__ == "__main__"
```

When imported into another file:

```python
__name__
```

contains the module's name.

Example:

```python
if __name__ == "__main__":
    print("Running directly")
```

This prevents certain code from running when the file is imported.

---

## Best Practices

- Use descriptive module names.
- Keep related functions together.
- Avoid importing everything using `from module import *`.
- Use aliases only when they improve readability.
- Organize reusable code into custom modules.
