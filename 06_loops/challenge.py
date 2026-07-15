"""
Challenge: Multiplication Table

Write a program that asks the user for a number
and prints its multiplication table from 1 to 10.
"""

number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
