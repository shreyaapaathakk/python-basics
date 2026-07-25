"""
Methods

This script demonstrates instance methods.
"""


class Student:
    """Represents a student."""

    def __init__(self, name):
        self.name = name

    def introduce(self):
        """Display student information."""

        print(f"My name is {self.name}.")


student = Student("Alice")

student.introduce()
