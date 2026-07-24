"""
Appending to Files

This script demonstrates how to append data to a file.
"""

file = open("sample.txt", "a")

file.write("\nThis line was added later.")

file.close()

print("Data appended successfully.")
