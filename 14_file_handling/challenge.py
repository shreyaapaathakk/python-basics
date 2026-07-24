"""
Mini Project: Simple Notes Manager

Concepts Used:
- File handling
- Reading files
- Writing files
- Appending files
- Loops
- Conditionals
"""

FILE_NAME = "notes.txt"

while True:
    print("\n===== Simple Notes Manager =====")
    print("1. View Notes")
    print("2. Add Note")
    print("3. Clear Notes")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            with open(FILE_NAME, "r") as file:
                content = file.read()

                if content.strip():
                    print("\nYour Notes")
                    print("-" * 30)
                    print(content)
                else:
                    print("No notes available.")

        except FileNotFoundError:
            print("No notes found. Add a note first.")

    elif choice == "2":
        note = input("Enter your note: ")

        with open(FILE_NAME, "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    elif choice == "3":
        with open(FILE_NAME, "w") as file:
            file.write("")

        print("All notes cleared.")

    elif choice == "4":
        print("Thank you for using the Simple Notes Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
