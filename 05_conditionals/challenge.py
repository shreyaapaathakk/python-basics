"""
Challenge: Age Category Checker

Write a program that asks the user for their age
and prints the appropriate category.
"""

age = int(input("Enter your age: "))

if age < 13:
    print("You are a Child.")
elif age < 20:
    print("You are a Teenager.")
elif age < 60:
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")

"""
Challenge: Student Grade Calculator

Write a program that:

1. Takes marks as input.
2. Displays the corresponding grade.
3. Prints whether the student passed or failed.
"""

marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print("Grade:", grade)

if marks >= 40:
    print("Status: Pass")
else:
    print("Status: Fail")
