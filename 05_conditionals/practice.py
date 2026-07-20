"""
Practice Exercises: Conditional Statements
"""

print("========== Exercise 1 ==========")
# Check whether a person is eligible to vote.

age = 22

if age >= 18:
    print("Eligible to vote.")


print("\n========== Exercise 2 ==========")
# Check whether a number is even or odd.

number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


print("\n========== Exercise 3 ==========")
# Find the largest of two numbers.

a = 25
b = 18

if a > b:
    print(a)
else:
    print(b)


print("\n========== Exercise 4 ==========")
# Determine a student's grade.

marks = 72

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")


print("\n========== Exercise 5 ==========")
# Check login eligibility.

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")


print("\n========== Exercise 6 ==========")
# Check whether a year is a leap year.

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


print("\n========== Exercise 7 ==========")
# Check whether a person is eligible for a discount.

is_student = True
age = 21

if is_student and age < 25:
    print("Eligible for Student Discount")
else:
    print("Not Eligible")
