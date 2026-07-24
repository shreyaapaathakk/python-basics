"""
Practice Solutions - File Handling
"""

print("=" * 10, "Exercise 1", "=" * 10)

file = open("sample.txt", "r")
print("File opened successfully.")
file.close()

print("=" * 10, "Exercise 2", "=" * 10)

with open("sample.txt", "r") as file:
    print(file.read())

print("=" * 10, "Exercise 3", "=" * 10)

with open("sample.txt", "r") as file:
    print(file.readline())

print("=" * 10, "Exercise 4", "=" * 10)

with open("practice.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

print("Data written successfully.")

print("=" * 10, "Exercise 5", "=" * 10)

with open("practice.txt", "a") as file:
    file.write("Line 4\n")

print("Data appended successfully.")

print("=" * 10, "Exercise 6", "=" * 10)

with open("practice.txt", "r") as file:
    print(file.read())

print("=" * 10, "Exercise 7", "=" * 10)

with open("practice.txt", "r") as file:
    print(file.tell())

print("=" * 10, "Exercise 8", "=" * 10)

with open("practice.txt", "r") as file:
    file.seek(0)
    print(file.read(5))

print("=" * 10, "Bonus Challenge", "=" * 10)

with open("practice.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)

print("File copied successfully.")
