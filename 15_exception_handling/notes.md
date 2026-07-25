# Python Exception Handling

## What is an Exception?

An exception is an error that occurs while a program is running.

Without exception handling, the program stops immediately when an error occurs.

---

## Why Use Exception Handling?

- Prevent program crashes
- Display user-friendly error messages
- Handle unexpected situations
- Improve program reliability

---

## try and except

```python
try:
    number = int(input())

except ValueError:
    print("Invalid input.")
```

---

## Common Exceptions

| Exception | Description |
|-----------|-------------|
| ValueError | Invalid value |
| TypeError | Wrong data type |
| ZeroDivisionError | Division by zero |
| IndexError | Invalid list index |
| KeyError | Missing dictionary key |
| FileNotFoundError | File does not exist |

---

## Handling Multiple Exceptions

```python
try:
    pass

except ValueError:
    pass

except ZeroDivisionError:
    pass
```

---

## else Block

Runs only if no exception occurs.

```python
try:
    pass

except ValueError:
    pass

else:
    print("Success")
```

---

## finally Block

Always executes.

```python
try:
    pass

finally:
    print("Finished")
```

Useful for:

- Closing files
- Releasing resources
- Cleaning up

---

## Raising Exceptions

```python
raise ValueError("Invalid value")
```

---

## Custom Exceptions

```python
class MyError(Exception):
    pass
```

Raise it:

```python
raise MyError("Something went wrong")
```

---

## Exception Flow

```
try
 │
 ├── No exception
 │      │
 │      ▼
 │     else
 │
 └── Exception
        │
        ▼
     except
        │
        ▼
     finally
```

---

## Best Practices

- Catch only the exceptions you expect.
- Avoid using a bare `except:`.
- Write clear error messages.
- Use `finally` for cleanup tasks.
- Create custom exceptions only when they improve code clarity.
