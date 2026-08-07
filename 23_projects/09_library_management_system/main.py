"""
Library Management System

A beginner-friendly console application to manage library books.

Features:
- Add books
- View books
- Search books
- Issue books
- Return books
- Delete books

Author: Your Name
"""

books = []


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 45)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")


def find_book(book_id):
    """
    Find a book using its ID.

    Args:
        book_id (str): The book ID.

    Returns:
        dict | None: Book record if found.
    """
    for book in books:
        if book["id"].lower() == book_id.lower():
            return book
    return None


def add_book():
    """Add a new book to the library."""

    book_id = input("\nEnter Book ID: ").strip()

    if not book_id:
        print("Book ID cannot be empty.")
        return

    if find_book(book_id):
        print("A book with this ID already exists.")
        return

    title = input("Enter Book Title: ").strip()

    if not title:
        print("Book title cannot be empty.")
        return

    author = input("Enter Author Name: ").strip()

    if not author:
        print("Author name cannot be empty.")
        return

    books.append(
        {
            "id": book_id,
            "title": title,
            "author": author,
            "available": True
        }
    )

    print("Book added successfully.")


def view_books():
    """Display all books."""

    if not books:
        print("\nNo books available.")
        return

    print("\nLibrary Books")
    print("-" * 55)

    for index, book in enumerate(books, start=1):
        status = "Available" if book["available"] else "Issued"

        print(f"{index}. ID        : {book['id']}")
        print(f"   Title     : {book['title']}")
        print(f"   Author    : {book['author']}")
        print(f"   Status    : {status}")
        print("-" * 55)


def search_book():
    """Search for a book by ID."""

    if not books:
        print("\nNo books available.")
        return

    book_id = input("\nEnter Book ID: ").strip()

    book = find_book(book_id)

    if book:
        status = "Available" if book["available"] else "Issued"

        print("\nBook Found")
        print(f"ID      : {book['id']}")
        print(f"Title   : {book['title']}")
        print(f"Author  : {book['author']}")
        print(f"Status  : {status}")
    else:
        print("Book not found.")


def issue_book():
    """Issue a book."""

    if not books:
        print("\nNo books available.")
        return

    book_id = input("\nEnter Book ID to issue: ").strip()

    book = find_book(book_id)

    if not book:
        print("Book not found.")
        return

    if not book["available"]:
        print("This book has already been issued.")
        return

    book["available"] = False
    print("Book issued successfully.")


def return_book():
    """Return an issued book."""

    if not books:
        print("\nNo books available.")
        return

    book_id = input("\nEnter Book ID to return: ").strip()

    book = find_book(book_id)

    if not book:
        print("Book not found.")
        return

    if book["available"]:
        print("This book is already available in the library.")
        return

    book["available"] = True
    print("Book returned successfully.")


def delete_book():
    """Delete a book."""

    if not books:
        print("\nNo books available.")
        return

    book_id = input("\nEnter Book ID to delete: ").strip()

    book = find_book(book_id)

    if book:
        books.remove(book)
        print("Book deleted successfully.")
    else:
        print("Book not found.")


def main():
    """Run the Library Management System."""

    while True:

        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                add_book()

            elif choice == 2:
                view_books()

            elif choice == 3:
                search_book()

            elif choice == 4:
                issue_book()

            elif choice == 5:
                return_book()

            elif choice == 6:
                delete_book()

            elif choice == 7:
                print("\nThank you for using Library Management System.")
                break

            else:
                print("Please choose a number between 1 and 7.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
