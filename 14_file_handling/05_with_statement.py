"""
Using the with Statement

This script demonstrates the recommended way to work with files.
"""

with open("sample.txt", "r") as file:
    content = file.read()

print(content)

print("The file was closed automatically.")
