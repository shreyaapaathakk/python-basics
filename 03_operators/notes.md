# Operators in Python

## Files in This Topic

| File | Description |
|------|-------------|
| `01_arithmetic.py` | Arithmetic operators |
| `02_assignment.py` | Assignment operators |
| `03_comparison.py` | Comparison operators |
| `04_logical.py` | Logical operators |
| `05_identity.py` | Identity operators |
| `06_membership.py` | Membership operators |
| `exercises.md` | Practice questions |
| `practice.py` | Solutions to the practice exercises |
| `challenge.py` | Mini project combining different operators |

## What is an Operator?

An operator is a symbol or keyword that performs an operation on one or more values (operands).

Example:

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

---

# Types of Operators

Python provides several categories of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators

---

## 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 2` |
| `-` | Subtraction | `5 - 2` |
| `*` | Multiplication | `5 * 2` |
| `/` | Division | `5 / 2` |
| `//` | Floor Division | `5 // 2` |
| `%` | Modulus | `5 % 2` |
| `**` | Exponent | `5 ** 2` |

---

## 2. Assignment Operators

Used to assign or update variable values.

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| `=` | `x = 5` | Assign value |
| `+=` | `x += 2` | `x = x + 2` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |

---

## 3. Comparison Operators

Comparison operators return a Boolean (`True` or `False`).

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## 4. Logical Operators

Used to combine or negate conditions.

| Operator | Description |
|----------|-------------|
| `and` | True if both conditions are true |
| `or` | True if at least one condition is true |
| `not` | Reverses a Boolean value |

Example:

```python
age = 20
has_id = True

print(age >= 18 and has_id)
```

---

## 5. Identity Operators

Identity operators compare whether two variables refer to the same object in memory.

| Operator | Description |
|----------|-------------|
| `is` | True if both variables refer to the same object |
| `is not` | True if they refer to different objects |

> **Note:** `is` checks object identity, while `==` checks whether values are equal.

---

## 6. Membership Operators

Membership operators test whether a value exists in a sequence.

| Operator | Description |
|----------|-------------|
| `in` | Value exists in the sequence |
| `not in` | Value does not exist in the sequence |

Example:

```python
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
```

---

## Best Practices

- Use descriptive variable names.
- Use parentheses to improve readability in complex expressions.
- Use `==` to compare values and `is` to compare object identity.
- Keep expressions simple and easy to understand.

---

## Key Takeaways

- Operators perform actions on values.
- Arithmetic operators are used for calculations.
- Assignment operators update variables.
- Comparison operators return `True` or `False`.
- Logical operators combine conditions.
- Identity operators compare object identity.
- Membership operators check whether a value exists in a sequence.
