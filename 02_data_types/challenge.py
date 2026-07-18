"""
Challenge: Student Profile

Create a program that:

1. Takes user input for:
   - Name
   - Age
   - Height
   - CGPA

2. Convert the numeric inputs to the correct data types.

3. Print the information along with the data type of each value.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in feet): "))
cgpa = float(input("Enter your CGPA: "))

print("\n===== Student Profile =====")
print(f"Name   : {name} ({type(name).__name__})")
print(f"Age    : {age} ({type(age).__name__})")
print(f"Height : {height} ({type(height).__name__})")
print(f"CGPA   : {cgpa} ({type(cgpa).__name__})")
