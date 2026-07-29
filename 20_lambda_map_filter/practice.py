"""
practice.py

Solutions for Lambda, Map, Filter & Reduce exercises.
"""

from functools import reduce

print("=" * 10, "Exercise 1", "=" * 10)

cube = lambda number: number ** 3
print(cube(4))


print("\n" + "=" * 10, "Exercise 2", "=" * 10)

numbers = [2, 4, 6, 8]
doubled = list(map(lambda number: number * 2, numbers))
print(doubled)


print("\n" + "=" * 10, "Exercise 3", "=" * 10)

numbers = [4, 8, 12, 16, 20]
greater_than_ten = list(filter(lambda number: number > 10, numbers))
print(greater_than_ten)


print("\n" + "=" * 10, "Exercise 4", "=" * 10)

numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)


print("\n" + "=" * 10, "Exercise 5", "=" * 10)

names = ["Alice", "Bob", "Charlotte", "David"]
sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)


print("\n" + "=" * 10, "Exercise 6", "=" * 10)

students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 95),
    ("David", 81),
]

sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)


print("\n" + "=" * 10, "Exercise 7", "=" * 10)

celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda temp: (temp * 9 / 5) + 32, celsius))
print(fahrenheit)


print("\n" + "=" * 10, "Bonus Challenge", "=" * 10)

students = [
    ("Alice", 45),
    ("Bob", 68),
    ("Charlie", 91),
    ("David", 52),
]

passed_students = list(filter(lambda student: student[1] >= 50, students))
updated_students = list(
    map(lambda student: (student[0], student[1] + 5), passed_students)
)
total_marks = reduce(lambda total, student: total + student[1], updated_students, 0)

print("Passed Students:", updated_students)
print("Total Marks:", total_marks)
