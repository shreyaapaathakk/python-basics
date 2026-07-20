# Conditional Statements in Python

## Files in This Topic

| File | Description |
|------|-------------|
| `01_if.py` | Basic `if` statement |
| `02_if_else.py` | Using `if...else` |
| `03_if_elif_else.py` | Multiple conditions with `elif` |
| `04_nested_if.py` | Nested conditional statements |
| `exercises.md` | Practice questions |
| `practice.py` | Solutions to the practice exercises |
| `challenge.py` | Student grade calculator mini project |

## What are Conditional Statements?

Conditional statements allow a program to make decisions based on whether a condition is `True` or `False`.

---

## The `if` Statement

Use `if` to execute a block of code only when a condition is true.

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

---

## The `if...else` Statement

Use `else` to define what happens when the condition is false.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## The `if...elif...else` Statement

Use `elif` (short for "else if") to check multiple conditions.

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

---

## Nested `if` Statements

An `if` statement can contain another `if` statement.

```python
is_student = True
age = 20

if is_student:
    if age < 25:
        print("Eligible for student discount.")
```

---

## Comparison Operators in Conditions

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## Logical Operators

Logical operators let you combine multiple conditions.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
```

| Operator | Meaning |
|----------|---------|
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses the condition |

---

## Indentation

Python uses indentation (spaces) to define code blocks.

```python
if True:
    print("Correct indentation")
```

Incorrect indentation causes an `IndentationError`.

---

## Best Practices

- Keep conditions simple and readable.
- Use meaningful variable names.
- Avoid deeply nested `if` statements when possible.
- Use `elif` instead of multiple separate `if` statements when checking related conditions.

---

## Practice Challenge

Write a program that:

1. Asks the user for their age.
2. Prints:
   - **Child** if age is less than 13
   - **Teenager** if age is between 13 and 19
   - **Adult** if age is between 20 and 59
   - **Senior Citizen** if age is 60 or above

---

## Key Takeaways

- `if` executes code when a condition is true.
- `else` handles the alternative case.
- `elif` checks additional conditions.
- Conditions evaluate to either `True` or `False`.
- Proper indentation is required in Python.
