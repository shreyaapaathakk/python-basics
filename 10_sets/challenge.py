"""
Mini Project: Student Club Manager

Concepts Used:
- Sets
- Loops
- Membership
- Set operations
"""

science_club = {"Alice", "Bob", "Charlie", "David"}
sports_club = {"Charlie", "David", "Emma", "Frank"}

print("===== Student Club Manager =====")

print("\nScience Club:")
for student in science_club:
    print(student)

print("\nSports Club:")
for student in sports_club:
    print(student)

print("\nStudents in Both Clubs:")
for student in science_club & sports_club:
    print(student)

print("\nOnly in Science Club:")
for student in science_club - sports_club:
    print(student)

print("\nOnly in Sports Club:")
for student in sports_club - science_club:
    print(student)

print("\nAll Club Members:")
for student in science_club | sports_club:
    print(student)
