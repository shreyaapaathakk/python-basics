"""
Practice Solutions - Lists
"""

print("=" * 10, "Exercise 1", "=" * 10)

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]
print(fruits)

print("=" * 10, "Exercise 2", "=" * 10)

print(fruits[0])
print(fruits[-1])

print("=" * 10, "Exercise 3", "=" * 10)

fruits[1] = "Kiwi"
print(fruits)

print("=" * 10, "Exercise 4", "=" * 10)

fruits.append("Pineapple")
fruits.append("Papaya")
print(fruits)

print("=" * 10, "Exercise 5", "=" * 10)

fruits.pop()
print(fruits)

print("=" * 10, "Exercise 6", "=" * 10)

numbers = [9, 3, 8, 2, 6]

numbers.sort()

print(numbers)

print("=" * 10, "Exercise 7", "=" * 10)

for fruit in fruits:
    print(fruit)

print("=" * 10, "Exercise 8", "=" * 10)

students = [
    ["Alice", 90],
    ["Bob", 85],
    ["Charlie", 95]
]

for student in students:
    print(student)

print("=" * 10, "Bonus Challenge", "=" * 10)

movies = [
    "Interstellar",
    "Inception",
    "Avatar",
    "Titanic",
    "The Matrix"
]

movies.sort()

print("Alphabetical:", movies)

print("Reverse:", movies[::-1])
