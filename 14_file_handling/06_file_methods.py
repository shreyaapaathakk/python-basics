"""
Useful File Methods

This script demonstrates commonly used file methods.
"""

with open("sample.txt", "r") as file:
    print("First Line:")
    print(file.readline())

with open("sample.txt", "r") as file:
    print("\nCurrent Position:", file.tell())

    file.read(5)

    print("Position After Reading:", file.tell())

    file.seek(0)

    print("Position After seek():", file.tell())
