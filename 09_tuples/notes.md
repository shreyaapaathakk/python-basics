# Python Tuples

## What is a Tuple?

A tuple is an ordered collection of items that **cannot be changed after it is created**.

Example:

```python
fruits = ("Apple", "Banana", "Orange")
```

---

## Features

- Ordered
- Immutable
- Allows duplicate values
- Can store different data types
- Faster than lists for fixed data

---

## Creating Tuples

```python
numbers = (1, 2, 3)
```

Empty tuple:

```python
empty = ()
```

Single-element tuple:

```python
single = ("Python",)
```

> **Note:** The comma is required when creating a tuple with one element.

---

## Accessing Items

```python
colors[0]
colors[-1]
colors[1:3]
```

---

## Tuple Operations

Concatenation

```python
tuple1 + tuple2
```

Repetition

```python
tuple1 * 3
```

Membership

```python
"Apple" in fruits
```

Length

```python
len(fruits)
```

---

## Tuple Methods

| Method | Description |
|---------|-------------|
| count() | Counts occurrences of a value |
| index() | Returns the index of a value |

Tuples have only **two built-in methods** because they are immutable.

---

## Tuple Unpacking

```python
student = ("Alice", 22)

name, age = student
```

Using the * operator:

```python
numbers = (1, 2, 3, 4)

first, *middle, last = numbers
```

---

## Nested Tuples

```python
students = (
    ("Alice", 90),
    ("Bob", 85)
)
```

---

## List vs Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses [] | Uses () |
| Many methods | Only count() and index() |
| Slightly slower | Slightly faster |

---

## Best Practices

- Use tuples for fixed data.
- Use lists for changing data.
- Store coordinates, dates, or records in tuples.
- Use meaningful variable names.
