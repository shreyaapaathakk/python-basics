"""
Practice Solutions - Strings
"""

print("=" * 10, "Exercise 1", "=" * 10)

name = "Alice"
print(name)

print("=" * 10, "Exercise 2", "=" * 10)

print(name[0])
print(name[-1])

print("=" * 10, "Exercise 3", "=" * 10)

language = "Programming"
print(language[:5])

print("=" * 10, "Exercise 4", "=" * 10)

text = "python"
print(text.upper())

print("=" * 10, "Exercise 5", "=" * 10)

sentence = "I like Java"
print(sentence.replace("Java", "Python"))

print("=" * 10, "Exercise 6", "=" * 10)

sentence = "Python is easy to learn"
print(sentence.split())

print("=" * 10, "Exercise 7", "=" * 10)

for character in "Python":
    print(character)

print("=" * 10, "Exercise 8", "=" * 10)

name = "Alice"
age = 20

print(f"My name is {name}. I am {age} years old.")

print("=" * 10, "Bonus Challenge", "=" * 10)

sentence = "Python programming is fun"

print("Characters:", len(sentence))
print("Words:", len(sentence.split()))
print("Upper:", sentence.upper())
print("Reverse:", sentence[::-1])
