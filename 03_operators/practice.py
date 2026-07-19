"""
Practice Exercises: Operators
"""

print("========== Exercise 1 ==========")
# Perform arithmetic operations.

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


print("\n========== Exercise 2 ==========")
# Use assignment operators.

score = 50

score += 10
score -= 5
score *= 2

print(score)


print("\n========== Exercise 3 ==========")
# Compare two numbers.

x = 20
y = 15

print(x > y)
print(x < y)
print(x == y)


print("\n========== Exercise 4 ==========")
# Use logical operators.

is_logged_in = True
has_subscription = False

print(is_logged_in and has_subscription)
print(is_logged_in or has_subscription)
print(not has_subscription)


print("\n========== Exercise 5 ==========")
# Identity operators.

list1 = [1, 2]
list2 = list1
list3 = [1, 2]

print(list1 is list2)
print(list1 == list3)


print("\n========== Exercise 6 ==========")
# Membership operators.

languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("JavaScript" not in languages)


print("\n========== Exercise 7 ==========")
# Mixed operators.

age = 20
marks = 85

print(age >= 18 and marks >= 80)
