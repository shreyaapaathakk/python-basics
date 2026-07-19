# Input and Output in Python

## Files in This Topic

| File | Description |
|------|-------------|
| `01_print.py` | Using the `print()` function |
| `02_input.py` | Reading user input with `input()` |
| `03_type_conversion.py` | Converting user input to different data types |
| `04_f_strings.py` | Formatting output using f-strings |
| `exercises.md` | Practice questions |
| `practice.py` | Solutions to the practice exercises |
| `challenge.py` | Personal profile generator mini project |

## What is Input?

Input allows a user to provide data while a program is running.

Python uses the built-in `input()` function to read user input.

```python
name = input("Enter your name: ")
```

The text inside the parentheses is called a **prompt**. It tells the user what to enter.

---

## What is Output?

Output is the information displayed by a program.

Python uses the built-in `print()` function.

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

---

## Reading User Input

```python
name = input("Enter your name: ")

print(name)
```

Sample Output:

```text
Enter your name: Alice
Alice
```

---

## Important: `input()` Always Returns a String

Even if the user enters a number, the value is stored as a string.

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

---

## Type Conversion

Convert input to other data types using built-in functions.

### Convert to Integer

```python
age = int(input("Enter your age: "))
```

### Convert to Float

```python
height = float(input("Enter your height: "))
```

### Convert to String

```python
number = 100

text = str(number)
```

---

## Printing Multiple Values

```python
name = "Alice"
age = 21

print(name, age)
```

Output:

```text
Alice 21
```

---

## Using f-Strings

An f-string lets you insert variables directly into a string.

```python
name = "Alice"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Alice and I am 21 years old.
```

---

## Escape Characters

| Escape Character | Meaning |
|------------------|---------|
| `\n` | New line |
| `\t` | Horizontal tab |
| `\"` | Double quote |
| `\\` | Backslash |

Example:

```python
print("Python\nProgramming")
```

Output:

```text
Python
Programming
```

---

## Common Mistakes

### Forgetting to Convert Input

```python
age = input("Enter your age: ")

print(age + 5)
```

This raises an error because `age` is a string.

Correct:

```python
age = int(input("Enter your age: "))

print(age + 5)
```

---

## Best Practices

- Write clear prompts.
- Convert user input to the appropriate data type.
- Use f-strings for readable output.
- Validate input when building larger applications.

---

## Key Takeaways

- `input()` reads data from the user.
- `print()` displays output.
- `input()` always returns a string.
- Use `int()` and `float()` to convert numeric input.
- f-strings make output cleaner and easier to read.
