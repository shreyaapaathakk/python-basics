"""
Quiz Game

A beginner-friendly console quiz application.

Features:
- Multiple-choice questions
- Score calculation
- Play again option

Author: Your Name
"""

questions = [
    {
        "question": "What is the output of print(type(10))?",
        "options": {
            "A": "int",
            "B": "float",
            "C": "str",
            "D": "bool"
        },
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "function",
            "B": "define",
            "C": "def",
            "D": "fun"
        },
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False values?",
        "options": {
            "A": "String",
            "B": "Boolean",
            "C": "Integer",
            "D": "List"
        },
        "answer": "B"
    },
    {
        "question": "Which loop is commonly used when the number of iterations is known?",
        "options": {
            "A": "while",
            "B": "repeat",
            "C": "loop",
            "D": "for"
        },
        "answer": "D"
    },
    {
        "question": "Which symbol is used for exponentiation in Python?",
        "options": {
            "A": "^",
            "B": "*",
            "C": "**",
            "D": "//"
        },
        "answer": "C"
    }
]


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("             QUIZ GAME")
    print("=" * 40)
    print("1. Start Quiz")
    print("2. Exit")


def start_quiz():
    """Start the quiz and calculate the score."""

    score = 0

    print("\nStarting Quiz...\n")

    for question_number, question in enumerate(questions, start=1):

        print("-" * 40)
        print(f"Question {question_number}")
        print(question["question"])
        print()

        for option, value in question["options"].items():
            print(f"{option}. {value}")

        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()

            if answer in ("A", "B", "C", "D"):
                break

            print("Please enter A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            correct_option = question["answer"]
            correct_answer = question["options"][correct_option]

            print(f"Wrong!")
            print(f"Correct Answer: {correct_option}. {correct_answer}\n")

    print("=" * 40)
    print("Quiz Completed")
    print("=" * 40)
    print(f"Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100

    print(f"Percentage: {percentage:.0f}%")

    if percentage == 100:
        print("Excellent!")
    elif percentage >= 80:
        print("Great job!")
    elif percentage >= 60:
        print("Good effort!")
    else:
        print("Keep practicing!")


def main():
    """Run the Quiz Game."""

    while True:

        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                start_quiz()

                while True:
                    play_again = input(
                        "\nWould you like to play again? (Y/N): "
                    ).strip().upper()

                    if play_again == "Y":
                        start_quiz()
                    elif play_again == "N":
                        break
                    else:
                        print("Please enter Y or N.")

            elif choice == 2:
                print("\nThank you for playing the Quiz Game.")
                break

            else:
                print("Please choose a number between 1 and 2.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
