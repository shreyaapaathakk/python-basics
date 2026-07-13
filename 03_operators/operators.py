"""
Python Operators

This script demonstrates the different types of operators in Python.
"""

print("=== Arithmetic Operators ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


print("\n=== Assignment Operators ===")

x = 5
print("Initial value:", x)

x += 3
print("After x += 3:", x)

x *= 2
print("After x *= 2:", x)

x -= 4
print("After x -= 4:", x)


print("\n=== Comparison Operators ===")

print("10 == 3:", a == b)
print("10 != 3:", a != b)
print("10 > 3 :", a > b)
print("10 < 3 :", a < b)
print("10 >= 3:", a >= b)
print("10 <= 3:", a <= b)


print("\n=== Logical Operators ===")

is_student = True
has_id = False

print("is_student and has_id:", is_student and has_id)
print("is_student or has_id :", is_student or has_id)
print("not is_student       :", not is_student)


print("\n=== Identity Operators ===")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 == list3:", list1 == list3)


print("\n=== Membership Operators ===")

fruits = ["apple", "banana", "mango"]

print("'apple' in fruits:", "apple" in fruits)
print("'grapes' in fruits:", "grapes" in fruits)
print("'banana' not in fruits:", "banana" not in fruits)
