# Python Lists

## What is a List?

A list is an ordered, mutable collection that can store multiple values.

Example:

```python
fruits = ["Apple", "Banana", "Orange"]
```

---

## Features

- Ordered
- Mutable (can be changed)
- Allows duplicate values
- Can store different data types

---

## Creating Lists

```python
numbers = [1, 2, 3]
```

```python
empty = []
```

```python
letters = list("Python")
```

---

## Accessing Items

```python
colors[0]
colors[-1]
```

---

## Modifying Lists

```python
numbers[1] = 100
```

---

## Adding Items

```python
append()
insert()
extend()
```

---

## Removing Items

```python
remove()
pop()
clear()
del
```

---

## Useful Methods

| Method | Description |
|---------|-------------|
| append() | Add item |
| insert() | Insert item |
| extend() | Add multiple items |
| remove() | Remove value |
| pop() | Remove by index |
| sort() | Sort list |
| reverse() | Reverse list |
| count() | Count occurrences |
| index() | Find position |
| clear() | Remove everything |

---

## List Slicing

```python
numbers[1:4]
numbers[:3]
numbers[-2:]
numbers[::-1]
```

---

## Looping

```python
for item in numbers:
    print(item)
```

---

## Nested Lists

```python
students = [
    ["Alice", 90],
    ["Bob", 80]
]
```

---

## Best Practices

- Use descriptive variable names.
- Keep similar data together.
- Avoid modifying a list while iterating over it.
- Prefer `append()` over repeated concatenation.
