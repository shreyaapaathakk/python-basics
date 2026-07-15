# Loops in Python

## What is a Loop?

A loop allows you to execute the same block of code multiple times.

Python mainly provides two types of loops:

- `for` loop
- `while` loop

---

# The `for` Loop

A `for` loop is used to iterate over a sequence such as a list, string, tuple, or range.

### Example

```python
for number in range(1, 6):
    print(number)
```

Output

```text
1
2
3
4
5
```

---

## The `range()` Function

The `range()` function generates a sequence of numbers.

```python
range(start, stop, step)
```

Examples

```python
range(5)
```

Produces:

```text
0 1 2 3 4
```

```python
range(1, 6)
```

Produces:

```text
1 2 3 4 5
```

```python
range(2, 11, 2)
```

Produces:

```text
2 4 6 8 10
```

---

## Looping Through a String

```python
for letter in "Python":
    print(letter)
```

---

## Looping Through a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

---

# The `while` Loop

A `while` loop runs as long as its condition is `True`.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# `break`

The `break` statement immediately exits the loop.

```python
for number in range(1, 11):
    if number == 6:
        break
    print(number)
```

---

# `continue`

The `continue` statement skips the current iteration and moves to the next one.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output

```text
1
2
4
5
```

---

# `else` with Loops

The `else` block executes if the loop completes normally (without a `break`).

```python
for number in range(1, 4):
    print(number)
else:
    print("Loop completed.")
```

---

## Infinite Loop

A `while` loop without updating its condition can run forever.

```python
while True:
    print("This runs forever.")
```

> Press **Ctrl + C** in the terminal to stop an infinite loop.

---

## Best Practices

- Use `for` loops when you know the number of iterations.
- Use `while` loops when the number of iterations depends on a condition.
- Avoid infinite loops unless they are intentional.
- Keep loop bodies simple and readable.

---

## Practice Challenge

Write a program that:

1. Takes a number from the user.
2. Prints its multiplication table from **1 to 10**.

### Sample Output

```text
Enter a number: 5

Multiplication Table of 5

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

## Key Takeaways

- `for` loops iterate over sequences.
- `while` loops repeat while a condition is true.
- `range()` generates a sequence of numbers.
- `break` exits a loop.
- `continue` skips the current iteration.
- `else` executes when a loop finishes without a `break`.
