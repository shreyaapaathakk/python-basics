"""
01_why_virtual_environment.py

Why do we need virtual environments?

This file explains the concept through printed examples.
"""

print("=" * 50)
print("WHY USE A VIRTUAL ENVIRONMENT?")
print("=" * 50)

print("""
Imagine you have two projects:

Project A
- Django 4.2

Project B
- Django 5.1

Without a virtual environment, both projects would share the
same global Python installation, causing version conflicts.

A virtual environment keeps each project's dependencies isolated.
""")
