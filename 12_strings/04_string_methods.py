"""
Common String Methods

This script demonstrates commonly used string methods.
"""

text = "python programming"

print("Original:", text)

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Capitalize:", text.capitalize())

sentence = "Apple,Banana,Orange"

print("Split:", sentence.split(","))

words = ["Python", "is", "fun"]

print("Join:", " ".join(words))

print("Replace:", text.replace("python", "Python"))

print("Starts with 'python':", text.startswith("python"))
print("Ends with 'ing':", text.endswith("ing"))
