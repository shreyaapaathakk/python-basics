"""
Mini Project: Text Analyzer

Concepts Used:
- Strings
- String methods
- Loops
- Conditionals
- f-strings
"""

print("===== Text Analyzer =====")

text = input("Enter a sentence: ").strip()

if text:
    print("\nAnalysis")
    print("-" * 30)

    print(f"Original Text : {text}")
    print(f"Uppercase     : {text.upper()}")
    print(f"Lowercase     : {text.lower()}")
    print(f"Title Case    : {text.title()}")
    print(f"Characters    : {len(text)}")
    print(f"Words         : {len(text.split())}")
    print(f"Reversed      : {text[::-1]}")

    vowel_count = 0

    for character in text.lower():
        if character in "aeiou":
            vowel_count += 1

    print(f"Vowels        : {vowel_count}")

else:
    print("You did not enter any text.")
