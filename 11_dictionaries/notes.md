# Python Dictionaries

## What is a Dictionary?

A dictionary is a collection of **key-value pairs**.

Example:

```python
student = {
    "name": "Alice",
    "age": 22
}
```

---

## Features

- Stores data as key-value pairs
- Mutable
- Ordered (Python 3.7+)
- Keys must be unique
- Values can be duplicated
- Fast lookups using keys

---

## Creating Dictionaries

```python
student = {
    "name": "Alice",
    "age": 22
}
```

Using `dict()`:

```python
person = dict(name="John", age=25)
```

---

## Accessing Values

```python
student["name"]
student.get("name")
```

Use `get()` when a key might not exist.

```python
student.get("city", "Not Found")
```

---

## Adding and Updating Items

```python
student["city"] = "Delhi"

student["age"] = 23
```

---

## Removing Items

```python
pop()

popitem()

del

clear()
```

---

## Useful Dictionary Methods

| Method | Description |
|---------|-------------|
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| get() | Returns value safely |
| update() | Updates dictionary |
| copy() | Creates a copy |
| pop() | Removes a key |
| clear() | Removes all items |

---

## Looping

Keys

```python
for key in student:
```

Values

```python
for value in student.values():
```

Items

```python
for key, value in student.items():
```

---

## Nested Dictionaries

```python
students = {
    "student1": {
        "name": "Alice",
        "marks": 90
    }
}
```

---

## List vs Tuple vs Set vs Dictionary

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| Ordered | ✅ | ✅ | ❌ | ✅ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ | Keys ❌ |
| Indexing | ✅ | ✅ | ❌ | Keys |

---

## Best Practices

- Use meaningful key names.
- Prefer `get()` when a key may not exist.
- Keep keys consistent.
- Use dictionaries to represent real-world objects.
