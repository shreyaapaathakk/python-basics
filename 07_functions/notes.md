# Functions in Python

## What is a Function?

A function is a reusable block of code that performs a specific task. Functions help make programs more organized, reduce repetition, and improve readability.

---

## Defining a Function

Use the `def` keyword to define a function.

```python
def greet():
    print("Hello!")
```

Call the function:

```python
greet()
```

---

## Function with Parameters

Parameters allow you to pass information to a function.

```python
def greet(name):
    print(f"Hello, {name}!")
```

```python
greet("Alice")
```

---

## Returning Values

Use the `return` statement to send a value back to the caller.

```python
def add(a, b):
    return a + b
```

```python
result = add(10, 20)

print(result)
```

---

## Default Parameters

You can provide default values for parameters.

```python
def introduce(name, country="India"):
    print(name, country)
```

```python
introduce("Shreya")
introduce("Alice", "Canada")
```

---

## Keyword Arguments

Keyword arguments let you specify which parameter each value belongs to.

```python
def student(name, age):
    print(name, age)

student(age=22, name="Shreya")
```

---

## Variable-Length Arguments

### `*args`

Use `*args` to pass multiple positional arguments.

```python
def total(*numbers):
    print(sum(numbers))
```

```python
total(10, 20, 30)
```

---

### `**kwargs`

Use `**kwargs` to pass multiple keyword arguments.

```python
def profile(**details):
    print(details)
```

```python
profile(name="Alice", age=21)
```

---

## Local and Global Variables

### Local Variable

A local variable is created inside a function and can only be used there.

```python
def example():
    message = "Hello"

example()
```

### Global Variable

A global variable is created outside a function and can be accessed throughout the program.

```python
message = "Hello"

def display():
    print(message)
```

---

## Why Use Functions?

- Avoid repeating code.
- Make programs easier to understand.
- Break large problems into smaller tasks.
- Improve code reusability.
- Simplify testing and debugging.

---

## Best Practices

- Give functions descriptive names.
- Keep functions focused on a single task.
- Return values instead of printing whenever possible.
- Write short, reusable functions.

---

## Practice Challenge

Create a calculator function that:

1. Accepts two numbers.
2. Accepts an operator (`+`, `-`, `*`, `/`).
3. Returns the calculated result.
4. Handles division by zero gracefully.

---

## Key Takeaways

- Functions are defined using `def`.
- Functions can accept parameters.
- `return` sends values back to the caller.
- Default parameters provide optional values.
- `*args` accepts multiple positional arguments.
- `**kwargs` accepts multiple keyword arguments.
- Functions make code reusable, organized, and easier to maintain.
