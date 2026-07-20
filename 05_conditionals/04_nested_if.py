"""
Nested if Statements

This script demonstrates nested if statements.
"""

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Please bring a valid ID.")
else:
    print("You must be at least 18 years old.")
