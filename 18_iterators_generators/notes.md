# Iterators and Generators

## Introduction

Whenever you use a loop like this:

```python
for item in my_list:
    print(item)
```

Python secretly creates an iterator.

---

# Iterable

An iterable is an object that can be looped over.

Examples:

- list
- tuple
- string
- dictionary
- set

Example:

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)
```

---

# Iterator

An iterator remembers its current position.

Create one using:

```python
iterator = iter(numbers)
```

Retrieve values using:

```python
next(iterator)
```

When all values are exhausted:

```
StopIteration
```

is raised.

---

# iter()

Converts an iterable into an iterator.

Example:

```python
colors = ["Red", "Blue", "Green"]

iterator = iter(colors)

print(next(iterator))
```

---

# next()

Returns the next value.

Example:

```python
print(next(iterator))
```

---

# Custom Iterator

To create one:

Implement

- `__iter__()`
- `__next__()`

Example:

```python
class Counter:
```

Python calls these methods automatically during iteration.

---

# Generator

A generator is a simpler way to create an iterator.

Instead of writing:

```python
__iter__()
__next__()
```

you simply use:

```python
yield
```

Example:

```python
def numbers():
    yield 1
    yield 2
```

---

# yield

`yield` pauses a function.

Next time the generator is called, execution continues from where it stopped.

Unlike `return`:

- return ends the function
- yield pauses the function

---

# Generator Expression

List comprehension:

```python
[x*x for x in range(5)]
```

Generator expression:

```python
(x*x for x in range(5))
```

Notice the parentheses.

---

# Memory Efficiency

List:

Stores every value in memory.

Generator:

Creates values one by one.

For large datasets, generators are much more memory efficient.

---

# Iterator vs Generator

| Iterator | Generator |
|-----------|-----------|
|Uses class|Uses function|
|Needs __iter__()|Uses yield|
|Needs __next__()|Automatically handled|
|More code|Less code|
|Reusable pattern|Quick implementation|

---

# Advantages of Generators

- Faster
- Uses less memory
- Easy to write
- Suitable for huge datasets
- Lazy evaluation

---

# Best Practices

- Prefer generators for large data.
- Use iter() only when necessary.
- Catch StopIteration only if manually calling next().
- Keep generators simple.
