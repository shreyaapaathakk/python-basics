# Python Strings

## What is a String?

A string is a sequence of characters enclosed in single, double, or triple quotes.

```python
name = "Python"
```

---

## Features

- Ordered
- Immutable
- Supports indexing and slicing
- Can contain letters, numbers, symbols, and spaces

---

## Creating Strings

```python
name = "Alice"

city = 'London'

message = """Welcome"""
```

---

## Indexing

```python
word = "Python"

word[0]

word[-1]
```

---

## Slicing

```python
word[:3]

word[2:5]

word[::-1]
```

---

## Common String Methods

| Method | Description |
|---------|-------------|
| upper() | Converts to uppercase |
| lower() | Converts to lowercase |
| title() | Converts to title case |
| capitalize() | Capitalizes the first letter |
| replace() | Replaces text |
| split() | Splits a string into a list |
| join() | Joins list items into a string |
| strip() | Removes leading and trailing spaces |
| startswith() | Checks the beginning |
| endswith() | Checks the ending |
| find() | Finds the first occurrence |
| count() | Counts occurrences |

---

## String Formatting

Using f-strings

```python
name = "Alice"

print(f"Hello, {name}")
```

Using format()

```python
print("Hello {}".format(name))
```

---

## Escape Characters

| Escape | Meaning |
|---------|---------|
| \n | New line |
| \t | Tab |
| \\ | Backslash |
| \" | Double quote |
| \' | Single quote |

---

## Looping

```python
for letter in word:
    print(letter)
```

---

## String Immutability

Strings cannot be modified directly.

```python
word = "Python"

# Not allowed
# word[0] = "J"

# Correct
word = "J" + word[1:]
```

---

## Best Practices

- Use meaningful variable names.
- Prefer f-strings for formatting.
- Remember that strings are immutable.
- Use built-in methods instead of writing custom code whenever possible.
