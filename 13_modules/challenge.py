"""
Mini Project: Random Password Generator

Concepts Used:
- Modules
- random module
- string module
- Functions
- Loops
"""

import random
import string

print("===== Random Password Generator =====")

length = int(input("Enter password length: "))

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ""

for _ in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)
