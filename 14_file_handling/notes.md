# Python File Handling

## What is File Handling?

File handling allows Python programs to create, read, update, and delete files.

---

## Opening a File

```python
file = open("sample.txt", "r")
```

Syntax

```python
open(filename, mode)
```

---

## File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default) |
| `"w"` | Write (creates or overwrites) |
| `"a"` | Append |
| `"x"` | Create a new file |
| `"b"` | Binary mode |
| `"t"` | Text mode (default) |

Examples

```python
open("file.txt", "r")
```

```python
open("file.txt", "w")
```

```python
open("image.png", "rb")
```

---

## Reading Files

Read the entire file

```python
file.read()
```

Read one line

```python
file.readline()
```

Read all lines

```python
file.readlines()
```

---

## Writing Files

```python
file.write("Hello")
```

> **Note:** Opening a file in `"w"` mode overwrites its existing contents.

---

## Appending Files

```python
file.write("New line")
```

Append mode (`"a"`) adds data without removing existing content.

---

## Closing Files

```python
file.close()
```

Always close files after using them.

---

## Using the with Statement

Recommended approach

```python
with open("sample.txt", "r") as file:
    data = file.read()
```

The file is closed automatically after leaving the `with` block.

---

## Useful File Methods

| Method | Description |
|---------|-------------|
| read() | Reads the whole file |
| readline() | Reads one line |
| readlines() | Reads all lines |
| write() | Writes data |
| tell() | Returns current cursor position |
| seek() | Moves the cursor |
| close() | Closes the file |

---

## Best Practices

- Prefer the `with` statement over manually calling `close()`.
- Choose the correct file mode.
- Close files when you're finished.
- Use meaningful file names.
- Handle possible errors (covered in the next module on exception handling).
