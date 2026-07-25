"""
Mini Project: Library Management System

Concepts Used:
- Classes and objects
- Constructors
- Instance methods
- Lists
- Loops
"""


class Book:
    """Represents a book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    """Represents a library."""

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nAvailable Books")
        print("-" * 30)

        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book.title} by {book.author}")


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
