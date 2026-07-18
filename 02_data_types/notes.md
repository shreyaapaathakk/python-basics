# Data Types in Python

## Files in This Topic

| File | Description |
|------|-------------|
| `01_basic_data_types.py` | Introduction to Python's built-in data types |
| `02_type_conversion.py` | Converting between different data types |
| `exercises.md` | Practice questions |
| `practice.py` | Solutions to the practice exercises |
| `challenge.py` | Mini project to apply what you've learned |

## What is a Data Type?

A data type defines the kind of value a variable stores. Python automatically determines the data type when you assign a value.

---

## Common Built-in Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| `int` | Whole numbers | `10`, `-5`, `1000` |
| `float` | Decimal numbers | `3.14`, `-0.5` |
| `str` | Text (strings) | `"Hello"` |
| `bool` | Boolean values | `True`, `False` |

---

## Integer (`int`)

Stores whole numbers.

```python
age = 22
temperature = -5
```

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

---

## Float (`float`)

Stores decimal numbers.

```python
price = 99.99
height = 5.7
```

Output:

```python
print(type(price))
```

```text
<class 'float'>
```

---

## String (`str`)

Stores text enclosed in single or double quotes.

```python
name = "Shreya"
language = 'Python'
```

Output:

```python
print(type(name))
```

```text
<class 'str'>
```

---

## Boolean (`bool`)

Represents logical values.

```python
is_logged_in = True
has_permission = False
```

Output:

```python
print(type(is_logged_in))
```

```text
<class 'bool'>
```

---

## Checking a Variable's Type

Use the built-in `type()` function.

```python
age = 22

print(type(age))
```

Output:

```text
<class 'int'>
```

---

## Type Conversion (Casting)

Python lets you convert one data type to another.

```python
age = "22"

print(int(age))
```

```python
price = 50

print(float(price))
```

```python
number = 123

print(str(number))
```

---

## Best Practices

- Choose meaningful variable names.
- Use the correct data type for the information you're storing.
- Use `type()` to inspect a variable when learning.
- Convert data types only when necessary.

---

## Key Takeaways

- Every value in Python has a data type.
- Python is dynamically typed, so you don't declare types explicitly.
- `type()` tells you a variable's data type.
- Common basic types are `int`, `float`, `str`, and `bool`.
- Python provides built-in functions like `int()`, `float()`, and `str()` for type conversion.
