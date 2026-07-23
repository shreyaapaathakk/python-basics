"""
Practice Solutions - Dictionaries
"""

print("=" * 10, "Exercise 1", "=" * 10)

person = {
    "name": "John",
    "age": 25,
    "city": "Mumbai"
}

print(person)

print("=" * 10, "Exercise 2", "=" * 10)

print(person["name"])

print("=" * 10, "Exercise 3", "=" * 10)

person["country"] = "India"
print(person)

print("=" * 10, "Exercise 4", "=" * 10)

person["age"] = 26
print(person)

print("=" * 10, "Exercise 5", "=" * 10)

person.pop("city")
print(person)

print("=" * 10, "Exercise 6", "=" * 10)

print("Keys:", person.keys())
print("Values:", person.values())

print("=" * 10, "Exercise 7", "=" * 10)

for key, value in person.items():
    print(f"{key}: {value}")

print("=" * 10, "Exercise 8", "=" * 10)

students = {
    "student1": {"name": "Alice", "marks": 90},
    "student2": {"name": "Bob", "marks": 85},
    "student3": {"name": "Charlie", "marks": 95}
}

for student_id, details in students.items():
    print(student_id, details)

print("=" * 10, "Bonus Challenge", "=" * 10)

books = {
    "Book 1": {
        "title": "Python Basics",
        "author": "John Smith",
        "price": 450
    },
    "Book 2": {
        "title": "Learning Python",
        "author": "Jane Doe",
        "price": 550
    },
    "Book 3": {
        "title": "Python Projects",
        "author": "Alice Brown",
        "price": 650
    }
}

for book, details in books.items():
    print(f"\n{book}")
    for key, value in details.items():
        print(f"{key.title()}: {value}")
