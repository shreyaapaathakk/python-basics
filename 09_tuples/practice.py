"""
Practice Solutions - Tuples
"""

print("=" * 10, "Exercise 1", "=" * 10)

colors = ("Red", "Green", "Blue", "Yellow", "Purple")
print(colors)

print("=" * 10, "Exercise 2", "=" * 10)

print(colors[0])
print(colors[-1])

print("=" * 10, "Exercise 3", "=" * 10)

single = ("Python",)
print(single)

print("=" * 10, "Exercise 4", "=" * 10)

tuple1 = (1, 2)
tuple2 = (3, 4)

result = tuple1 + tuple2
print(result)

print("=" * 10, "Exercise 5", "=" * 10)

numbers = (5, 10)

print(numbers * 3)

print("=" * 10, "Exercise 6", "=" * 10)

print(len(numbers))

print("=" * 10, "Exercise 7", "=" * 10)

student = ("Alice", 22)

name, age = student

print(name)
print(age)

print("=" * 10, "Exercise 8", "=" * 10)

students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
)

for student in students:
    print(student)

print("=" * 10, "Bonus Challenge", "=" * 10)

months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

month_number = 8

print("Month:", months[month_number - 1])
