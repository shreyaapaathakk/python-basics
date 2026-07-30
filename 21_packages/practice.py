"""
practice.py

Solutions for package exercises.
"""

from my_package import add, is_even
from my_package.calculator import multiply
import my_package.greetings as greetings

print("=" * 10, "Exercise 1", "=" * 10)
print("Created package: my_package")


print("\n" + "=" * 10, "Exercise 2", "=" * 10)
print("Example module: calculator.py")


print("\n" + "=" * 10, "Exercise 3", "=" * 10)
print(add(10, 20))


print("\n" + "=" * 10, "Exercise 4", "=" * 10)
print("Functions exported through __init__.py")


print("\n" + "=" * 10, "Exercise 5", "=" * 10)
print(greetings.say_hello("Alice"))


print("\n" + "=" * 10, "Exercise 6", "=" * 10)
print("Example additional module: statistics.py")


print("\n" + "=" * 10, "Exercise 7", "=" * 10)
print(multiply(8, 9))
print(is_even(18))


print("\n" + "=" * 10, "Bonus Challenge", "=" * 10)

temperature = {
    "celsius": 25,
    "fahrenheit": (25 * 9 / 5) + 32,
}

print(temperature)
