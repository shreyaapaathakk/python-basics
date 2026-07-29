# Lambda, Map, Filter & Reduce

## Introduction

Python supports a functional programming style using tools like:

- lambda
- map()
- filter()
- reduce()

These tools help write concise and readable code for common data-processing tasks.

---

# Lambda Function

A lambda function is a small anonymous function.

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x ** 2

print(square(4))
```

Equivalent to:

```python
def square(x):
    return x ** 2
```

Use lambda when the function is short and used only once.

---

# map()

`map()` applies a function to every item in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

Output:

```
[2, 4, 6]
```

---

# filter()

`filter()` selects items that satisfy a condition.

Syntax:

```python
filter(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]

even = filter(lambda x: x % 2 == 0, numbers)

print(list(even))
```

Output:

```
[2, 4]
```

---

# reduce()

`reduce()` repeatedly combines values into a single result.

It is available in the `functools` module.

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, numbers)

print(total)
```

Output:

```
10
```

---

# Sorting with Lambda

The `key` parameter accepts a function.

Example:

```python
students.sort(key=lambda student: student[1])
```

This sorts by the second value (marks).

---

# Lambda vs Regular Function

| Lambda | Regular Function |
|---------|------------------|
|Anonymous|Named|
|One expression|Multiple statements|
|Short|Longer|
|Good for temporary use|Reusable|

---

# Advantages

- Less code
- Readable for simple operations
- Useful with map(), filter(), sorted()

---

# Limitations

- Only one expression
- Not suitable for complex logic
- Harder to debug if overused

---

# Best Practices

- Keep lambda functions short.
- Use regular functions for complex operations.
- Prefer list comprehensions when they improve readability.
- Avoid deeply nested lambda expressions.

---

# Summary

- `lambda` creates anonymous functions.
- `map()` transforms data.
- `filter()` selects data.
- `reduce()` combines data.
- Lambda functions are commonly used with sorting.
