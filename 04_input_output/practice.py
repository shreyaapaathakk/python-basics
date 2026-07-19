"""
Practice Exercises: Input & Output
"""

print("========== Exercise 1 ==========")
# Print a welcome message.

print("Welcome to Python Programming!")


print("\n========== Exercise 2 ==========")
# Ask the user for their name and greet them.

name = input("Enter your name: ")

print(f"Hello, {name}!")


print("\n========== Exercise 3 ==========")
# Ask the user for two numbers and print their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)


print("\n========== Exercise 4 ==========")
# Ask the user for their height and display its data type.

height = float(input("Enter your height: "))

print(height)
print(type(height))


print("\n========== Exercise 5 ==========")
# Display information using an f-string.

city = input("Enter your city: ")
country = input("Enter your country: ")

print(f"You live in {city}, {country}.")
