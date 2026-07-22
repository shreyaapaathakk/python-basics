"""
Practice Solutions - Sets
"""

print("=" * 10, "Exercise 1", "=" * 10)

fruits = {"Apple", "Banana", "Orange", "Mango", "Grapes"}
print(fruits)

print("=" * 10, "Exercise 2", "=" * 10)

numbers = {1, 2, 2, 3, 3, 4, 5}
print(numbers)

print("=" * 10, "Exercise 3", "=" * 10)

fruits.add("Kiwi")
fruits.add("Papaya")
print(fruits)

print("=" * 10, "Exercise 4", "=" * 10)

fruits.remove("Banana")
print(fruits)

print("=" * 10, "Exercise 5", "=" * 10)

fruits.discard("Pineapple")
print(fruits)

print("=" * 10, "Exercise 6", "=" * 10)

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)

print("=" * 10, "Exercise 7", "=" * 10)

print(set_a & set_b)

print("=" * 10, "Exercise 8", "=" * 10)

numbers = frozenset([1, 2, 3, 4])
print(numbers)

print("=" * 10, "Bonus Challenge", "=" * 10)

friend1 = {"Reading", "Music", "Cricket"}
friend2 = {"Music", "Football", "Reading"}

print("Common:", friend1 & friend2)
print("Only Friend 1:", friend1 - friend2)
print("Only Friend 2:", friend2 - friend1)
print("All Hobbies:", friend1 | friend2)
