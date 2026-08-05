"""
Student Management System

A beginner-friendly console application to manage student records.

Features:
- Add students
- View students
- Search students
- Update student details
- Delete students

Author: Your Name
"""

students = []


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def find_student(student_id):
    """
    Search for a student by ID.

    Args:
        student_id (str): Student ID.

    Returns:
        dict | None: Student record if found.
    """
    for student in students:
        if student["id"].lower() == student_id.lower():
            return student
    return None


def add_student():
    """Add a new student."""

    student_id = input("\nEnter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(student_id):
        print("A student with this ID already exists.")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        age = int(input("Enter Age: "))

        if age <= 0:
            print("Age must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    course = input("Enter Course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    students.append(
        {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }
    )

    print("Student added successfully.")


def view_students():
    """Display all student records."""

    if not students:
        print("\nNo student records available.")
        return

    print("\nStudent Records")
    print("-" * 50)

    for index, student in enumerate(students, start=1):
        print(f"{index}. ID     : {student['id']}")
        print(f"   Name   : {student['name']}")
        print(f"   Age    : {student['age']}")
        print(f"   Course : {student['course']}")
        print("-" * 50)


def search_student():
    """Search for a student by ID."""

    if not students:
        print("\nNo student records available.")
        return

    student_id = input("\nEnter Student ID: ").strip()

    student = find_student(student_id)

    if student:
        print("\nStudent Found")
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
    else:
        print("Student not found.")


def update_student():
    """Update student information."""

    if not students:
        print("\nNo student records available.")
        return

    student_id = input("\nEnter Student ID to update: ").strip()

    student = find_student(student_id)

    if not student:
        print("Student not found.")
        return

    print("\nLeave a field blank to keep the current value.")

    new_name = input(f"Name ({student['name']}): ").strip()

    new_age = input(f"Age ({student['age']}): ").strip()

    new_course = input(f"Course ({student['course']}): ").strip()

    if new_name:
        student["name"] = new_name

    if new_age:
        try:
            age = int(new_age)

            if age > 0:
                student["age"] = age
            else:
                print("Invalid age. Previous value retained.")

        except ValueError:
            print("Invalid age. Previous value retained.")

    if new_course:
        student["course"] = new_course

    print("Student updated successfully.")


def delete_student():
    """Delete a student record."""

    if not students:
        print("\nNo student records available.")
        return

    student_id = input("\nEnter Student ID to delete: ").strip()

    student = find_student(student_id)

    if student:
        students.remove(student)
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def main():
    """Run the Student Management System."""

    while True:

        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                view_students()

            elif choice == 3:
                search_student()

            elif choice == 4:
                update_student()

            elif choice == 5:
                delete_student()

            elif choice == 6:
                print("\nThank you for using Student Management System.")
                break

            else:
                print("Please choose a number between 1 and 6.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
