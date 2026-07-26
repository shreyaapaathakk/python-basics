"""
Magic Methods

This script demonstrates common magic methods.
"""


class Book:
    """Represents a book."""

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return len(self.title)


book = Book("Python Basics")

print(book)

print(len(book))
