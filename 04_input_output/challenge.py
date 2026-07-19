## Practice Challenge

### Challenge 1

Write a program that:

1. Asks the user for their name.
2. Asks for their favorite programming language.
3. Asks how many hours they study each week.
4. Prints a personalized message using an f-string.

### Example Output

```text
Enter your name: Shreya
Favorite programming language: Python
Hours studied per week: 12

Hello, Shreya!
It's great that you're learning Python.
Studying 12 hours a week is a great habit. Keep it up!
```

"""
Challenge 2: Personal Profile Generator

Create a program that asks the user for:

- Name
- Age
- City
- Favorite Programming Language

Display the information using an f-string.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
language = input("Enter your favorite programming language: ")

print("\n===== Personal Profile =====")
print(
    f"""
Name      : {name}
Age       : {age}
City      : {city}
Language  : {language}
"""
)
