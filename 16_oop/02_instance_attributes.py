"""
Instance Attributes

This script demonstrates instance attributes.
"""


class Student:
    """Represents a student."""

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Alice", 20)

print(student.name)
print(student.age)
