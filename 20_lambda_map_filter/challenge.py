"""
Challenge Project

Student Result Analyzer

Objective:
Analyze student marks using lambda, map(), filter(), and reduce().
"""

from functools import reduce


def main():
    """Run the Student Result Analyzer."""

    students = [
        {"name": "Alice", "marks": 78},
        {"name": "Bob", "marks": 45},
        {"name": "Charlie", "marks": 92},
        {"name": "David", "marks": 61},
        {"name": "Eva", "marks": 39},
    ]

    passing_students = list(
        filter(lambda student: student["marks"] >= 50, students)
    )

    bonus_marks = list(
        map(
            lambda student: {
                "name": student["name"],
                "marks": student["marks"] + 5,
            },
            passing_students,
        )
    )

    total_marks = reduce(
        lambda total, student: total + student["marks"],
        bonus_marks,
        0,
    )

    print("Students Who Passed")
    print("-" * 25)

    for student in bonus_marks:
        print(f"{student['name']}: {student['marks']}")

    print("\nTotal Marks:", total_marks)


if __name__ == "__main__":
    main()
