# Variables in Python

## What is a Variable?

A variable is a named container used to store data in memory. You can think of it as a label that refers to a value.

## Syntax

```python
variable_name = value
```

### Examples

```python
name = "Shreya"
age = 22
height = 5.7
is_student = True
```

## Variable Naming Rules

- Variable names can contain letters, numbers, and underscores (`_`).
- A variable name **cannot** start with a number.
- Variable names are **case-sensitive**.
- Avoid using Python keywords as variable names.

### Valid Variable Names

```python
name = "Alice"
student_age = 21
_marks = 95
total2 = 100
```

### Invalid Variable Names

```python
2name = "Alice"      # Starts with a number
my-name = "Alice"    # Hyphen is not allowed
class = "Python"     # 'class' is a reserved keyword
```

## Common Data Types Stored in Variables

| Data Type | Example |
|-----------|---------|
| Integer (`int`) | `age = 22` |
| Float (`float`) | `height = 5.7` |
| String (`str`) | `name = "Shreya"` |
| Boolean (`bool`) | `is_student = True` |

## Reassigning Variables

Variables can be updated at any time.

```python
count = 10
print(count)

count = 20
print(count)
```

Output:

```text
10
20
```

## Multiple Assignment

Assign multiple variables in a single line.

```python
x, y, z = 1, 2, 3
```

Assign the same value to multiple variables.

```python
a = b = c = 100
```

## Best Practices

- Use meaningful variable names.
- Follow the `snake_case` naming convention.
- Keep names short but descriptive.
- Avoid single-letter names except for simple loops or temporary variables.

### Good Examples

```python
student_name = "Alice"
total_marks = 450
is_logged_in = False
```

### Poor Examples

```python
x = "Alice"
a = 450
t = False
```

## Key Takeaways

- Variables store data in memory.
- Variables are created when a value is assigned.
- Python is dynamically typed, so you don't need to declare a variable's type.
- Variables can be reassigned with new values.
- Use clear and descriptive names to make your code easier to read.
