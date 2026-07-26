"""
Class Methods

This script demonstrates class methods.
"""


class Student:
    """Represents a student."""

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        """Change the school name."""

        cls.school = new_school


student1 = Student("Alice")
student2 = Student("Bob")

print(Student.school)

Student.change_school("XYZ School")

print(student1.school)
print(student2.school)
