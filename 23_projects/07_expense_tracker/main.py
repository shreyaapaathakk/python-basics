"""
Expense Tracker

A beginner-friendly console application to manage daily expenses.

Features:
- Add expenses
- View all expenses
- Calculate total expenses
- Search expenses by category
- Delete expenses

Author: Your Name
"""

expenses = []


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("          EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Exit")


def add_expense():
    """Add a new expense."""

    title = input("\nEnter expense title: ").strip()

    if not title:
        print("Expense title cannot be empty.")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    expenses.append(
        {
            "title": title,
            "category": category,
            "amount": amount
        }
    )

    print("Expense added successfully.")


def view_expenses():
    """Display all recorded expenses."""

    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\nRecorded Expenses")
    print("-" * 55)

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['title']}")
        print(f"   Category : {expense['category']}")
        print(f"   Amount   : ₹{expense['amount']:.2f}")
        print("-" * 55)


def view_total_expenses():
    """Calculate and display total expenses."""

    if not expenses:
        print("\nNo expenses recorded.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total:.2f}")


def search_by_category():
    """Search expenses by category."""

    if not expenses:
        print("\nNo expenses recorded.")
        return

    category = input("\nEnter category to search: ").strip().lower()

    found = False

    print("\nMatching Expenses")
    print("-" * 55)

    for expense in expenses:
        if expense["category"].lower() == category:
            found = True
            print(f"Title    : {expense['title']}")
            print(f"Category : {expense['category']}")
            print(f"Amount   : ₹{expense['amount']:.2f}")
            print("-" * 55)

    if not found:
        print("No expenses found in this category.")


def delete_expense():
    """Delete an expense."""

    if not expenses:
        print("\nNo expenses recorded.")
        return

    view_expenses()

    try:
        expense_number = int(input("\nEnter expense number to delete: "))

        if 1 <= expense_number <= len(expenses):
            removed = expenses.pop(expense_number - 1)
            print(f"'{removed['title']}' deleted successfully.")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Run the Expense Tracker application."""

    while True:

        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                add_expense()

            elif choice == 2:
                view_expenses()

            elif choice == 3:
                view_total_expenses()

            elif choice == 4:
                search_by_category()

            elif choice == 5:
                delete_expense()

            elif choice == 6:
                print("\nThank you for using Expense Tracker.")
                break

            else:
                print("Please choose a number between 1 and 6.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
