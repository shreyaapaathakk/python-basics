"""
Mini Project: Student Information System

Concepts Used:
- Dictionaries
- Loops
- Conditionals
- Dictionary methods
"""

students = {}

while True:
    print("\n===== Student Information System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_number = input("Enter roll number: ")

        students[roll_number] = {
            "name": input("Enter student name: "),
            "age": input("Enter age: "),
            "course": input("Enter course: ")
        }

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records available.")
        else:
            print("\nStudent Records")
            for roll_number, details in students.items():
                print(f"\nRoll Number: {roll_number}")
                for key, value in details.items():
                    print(f"{key.title()}: {value}")

    elif choice == "3":
        roll_number = input("Enter roll number to search: ")

        if roll_number in students:
            print("\nStudent Found")
            for key, value in students[roll_number].items():
                print(f"{key.title()}: {value}")
        else:
            print("Student not found.")

    elif choice == "4":
        roll_number = input("Enter roll number to remove: ")

        if roll_number in students:
            students.pop(roll_number)
            print("Student removed successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you for using the Student Information System!")
        break

    else:
        print("Invalid choice. Please try again.")
