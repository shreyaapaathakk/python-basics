"""
05_relative_imports.py

Understanding absolute and relative imports.

This file demonstrates how modules inside the same package
can import each other.
"""

print("=" * 40)
print("ABSOLUTE VS RELATIVE IMPORTS")
print("=" * 40)

print("\nAbsolute Import Example")
print("-" * 25)

print(
    "from my_package.calculator import add\n"
    "result = add(10, 5)"
)

print("\nRelative Import Example")
print("-" * 25)

print(
    "from .calculator import add\n"
    "result = add(10, 5)"
)

print("\nExplanation")
print("-" * 25)

print("Absolute imports start from the project's top-level package.")
print("Relative imports use dots (.) to refer to the current package.")

print("\nDot Notation")
print("-" * 25)

print(".   -> Current package")
print("..  -> Parent package")
print("... -> Grandparent package")

print("\nWhen to Use Relative Imports")
print("-" * 25)

print("• Importing modules inside the same package.")
print("• Keeping package code portable.")
print("• Avoiding long import statements.")

print("\nWhen to Use Absolute Imports")
print("-" * 25)

print("• Importing from another package.")
print("• Application entry-point scripts.")
print("• Improving readability in larger projects.")

print("\nNote")
print("-" * 25)

print(
    "Relative imports work only when the file is executed "
    "as part of a package, not as a standalone script."
)
