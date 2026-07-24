"""
Reading Files

This script demonstrates different ways to read a file.
"""

file = open("sample.txt", "r")

# Read the entire file
print(file.read())

# Move the cursor back to the beginning
file.seek(0)

# Read one line
print(file.readline())

file.seek(0)

# Read all lines
print(file.readlines())

file.close()
