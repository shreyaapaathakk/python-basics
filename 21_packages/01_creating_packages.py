"""
01_creating_packages.py

Using functions from a package.
"""

from my_package.calculator import add
from my_package.greetings import say_hello

print(add(10, 5))
print(say_hello("Alice"))
