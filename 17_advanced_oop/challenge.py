"""
Mini Project: Student Management System

Concepts Used:
- Classes and objects
- Class variables
- Instance variables
- Class methods
- Static methods
- Properties
- Inheritance
- Method overriding
- super()
- Magic methods
- Exception handling
"""


class Person:
    """Base class representing a person."""

    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display(self):
        """Display person details."""
        print(f"ID   : {self.student_id}")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):
    """Represents a student."""

    total_students = 0

    def __init__(self, student_id, name, age, course):
        super().__init__(student_id, name, age)
        self._course = course
        Student.total_students += 1

    @property
    def course(self):
        """Return the course name."""
        return self._course

    @course.setter
    def course(self, value):
        if not value.strip():
            raise ValueError("Course name cannot be empty.")

        self._course = value

    @classmethod
    def student_count(cls):
        """Display total students."""
        print(f"Total Students: {cls.total_students}")

    @staticmethod
    def is_valid_age(age):
        """Return True if the age is valid."""
        return age >= 5

    def display(self):
        """Display student details."""
        super().display()
        print(f"Course: {self.course}")

    def __str__(self):
        return (
            f"{self.student_id} - "
            f"{self.name} ({self.course})"
        )


students = []


def add_student():
    """Add a student."""

    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        if not Student.is_valid_age(age):
            raise ValueError("Invalid age.")

        student = Student(
            student_id,
            name,
            age,
            course
        )

        students.append(student)

        print("Student added successfully!")

    except ValueError as error:
        print("Error:", error)


def view_students():
    """Display all students."""

    if not students:
        print("No student records found.")
        return

    print("\n===== Student Records =====")

    for student in students:
        print(student)
        print("-" * 30)


def search_student():
    """Search a student by ID."""

    student_id = input("Enter Student ID: ")

    for student in students:
        if student.student_id == student_id:
            print("\nStudent Found")
            print("-" * 30)
            student.display()
            return

    print("Student not found.")


def update_course():
    """Update a student's course."""

    student_id = input("Enter Student ID: ")

    for student in students:
        if student.student_id == student_id:

            try:
                student.course = input("Enter New Course: ")
                print("Course updated successfully!")

            except ValueError as error:
                print("Error:", error)

            return

    print("Student not found.")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Course")
    print("5. Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_course()

    elif choice == "5":
        Student.student_count()

    elif choice == "6":
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
