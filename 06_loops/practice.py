"""
Practice Exercises: Loops
"""

print("========== Exercise 1 ==========")
# Print numbers from 1 to 10.

for number in range(1, 11):
    print(number)


print("\n========== Exercise 2 ==========")
# Print even numbers from 2 to 20.

for number in range(2, 21, 2):
    print(number)


print("\n========== Exercise 3 ==========")
# Find the sum of numbers from 1 to 100.

total = 0

for number in range(1, 101):
    total += number

print("Sum:", total)


print("\n========== Exercise 4 ==========")
# Print a multiplication table.

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


print("\n========== Exercise 5 ==========")
# Countdown using a while loop.

count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast Off!")


print("\n========== Exercise 6 ==========")
# Print only odd numbers using continue.

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)


print("\n========== Exercise 7 ==========")
# Star pattern.

for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")

    print()
