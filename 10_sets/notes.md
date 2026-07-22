# Python Sets

## What is a Set?

A set is an unordered collection of unique items.

Example:

```python
fruits = {"Apple", "Banana", "Orange"}
```

---

## Features

- Unordered
- Mutable
- No duplicate values
- Fast membership testing

---

## Creating Sets

```python
numbers = {1, 2, 3}
```

Empty set:

```python
empty = set()
```

> **Note:** `{}` creates an empty dictionary, not an empty set.

---

## Adding Items

```python
add()
update()
```

---

## Removing Items

```python
remove()
discard()
pop()
clear()
```

| Method | Description |
|---------|-------------|
| remove() | Removes an item (raises an error if not found) |
| discard() | Removes an item (does nothing if not found) |
| pop() | Removes a random item |
| clear() | Removes all items |

---

## Set Operations

Union

```python
set1 | set2
```

Intersection

```python
set1 & set2
```

Difference

```python
set1 - set2
```

Symmetric Difference

```python
set1 ^ set2
```

---

## Membership

```python
"Apple" in fruits
```

---

## Frozen Sets

A `frozenset` is an immutable version of a set.

```python
numbers = frozenset([1, 2, 3])
```

---

## List vs Tuple vs Set

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Ordered | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ |
| Duplicates Allowed | ✅ | ✅ | ❌ |
| Indexing | ✅ | ✅ | ❌ |

---

## Best Practices

- Use sets when duplicate values are not needed.
- Use sets for fast membership testing.
- Use set operations to compare collections.
- Remember that sets are unordered.
