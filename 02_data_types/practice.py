"""
Practice Exercises: Data Types
"""

print("========== Exercise 1 ==========")
# Create variables of different data types.

age = 22
price = 99.99
language = "Python"
is_learning = True

print(type(age))
print(type(price))
print(type(language))
print(type(is_learning))


print("\n========== Exercise 2 ==========")
# Convert a string to an integer.

number = "50"

converted_number = int(number)

print(converted_number)
print(type(converted_number))


print("\n========== Exercise 3 ==========")
# Convert an integer to a float.

marks = 88

converted_marks = float(marks)

print(converted_marks)
print(type(converted_marks))


print("\n========== Exercise 4 ==========")
# Convert a float to an integer.

temperature = 36.8

converted_temperature = int(temperature)

print(converted_temperature)
print(type(converted_temperature))


print("\n========== Exercise 5 ==========")
# Convert an integer to a string.

roll_number = 101

converted_roll = str(roll_number)

print(converted_roll)
print(type(converted_roll))


print("\n========== Exercise 6 ==========")
# Explore boolean conversion.

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))


print("\n========== Exercise 7 ==========")
# Display both value and data type.

city = "Delhi"
population = 32900000

print(city, type(city))
print(population, type(population))
