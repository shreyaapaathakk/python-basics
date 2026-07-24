"""
Writing Files

This script demonstrates how to write to a file.
"""

file = open("sample.txt", "w")

file.write("Welcome to Python File Handling.\n")
file.write("This file was created using Python.")

file.close()

print("Data written successfully.")
