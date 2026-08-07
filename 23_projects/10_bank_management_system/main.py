"""
Bank Management System

A beginner-friendly console application that simulates
basic banking operations.

Features:
- Create account
- View account
- Deposit money
- Withdraw money
- Check balance
- View transaction history

Author: Your Name
"""

account = None


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 45)
    print("       BANK MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Exit")


def create_account():
    """Create a new bank account."""

    global account

    if account is not None:
        print("An account already exists.")
        return

    account_number = input("\nEnter Account Number: ").strip()

    if not account_number:
        print("Account number cannot be empty.")
        return

    holder_name = input("Enter Account Holder Name: ").strip()

    if not holder_name:
        print("Account holder name cannot be empty.")
        return

    try:
        initial_balance = float(input("Enter Initial Deposit: ₹"))

        if initial_balance < 0:
            print("Initial deposit cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    account = {
        "account_number": account_number,
        "holder_name": holder_name,
        "balance": initial_balance,
        "transactions": [
            f"Account created with ₹{initial_balance:.2f}"
        ]
    }

    print("Account created successfully.")


def view_account():
    """Display account information."""

    if account is None:
        print("\nNo account found.")
        return

    print("\nAccount Details")
    print("-" * 40)
    print(f"Account Number : {account['account_number']}")
    print(f"Account Holder : {account['holder_name']}")
    print(f"Balance        : ₹{account['balance']:.2f}")


def deposit_money():
    """Deposit money into the account."""

    if account is None:
        print("\nNo account found.")
        return

    try:
        amount = float(input("\nEnter deposit amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        account["balance"] += amount
        account["transactions"].append(
            f"Deposited ₹{amount:.2f}"
        )

        print("Deposit successful.")

    except ValueError:
        print("Please enter a valid amount.")


def withdraw_money():
    """Withdraw money from the account."""

    if account is None:
        print("\nNo account found.")
        return

    try:
        amount = float(input("\nEnter withdrawal amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > account["balance"]:
            print("Insufficient balance.")
            return

        account["balance"] -= amount

        account["transactions"].append(
            f"Withdrew ₹{amount:.2f}"
        )

        print("Withdrawal successful.")

    except ValueError:
        print("Please enter a valid amount.")


def check_balance():
    """Display current account balance."""

    if account is None:
        print("\nNo account found.")
        return

    print(f"\nCurrent Balance: ₹{account['balance']:.2f}")


def transaction_history():
    """Display all transactions."""

    if account is None:
        print("\nNo account found.")
        return

    print("\nTransaction History")
    print("-" * 40)

    for index, transaction in enumerate(
        account["transactions"],
        start=1
    ):
        print(f"{index}. {transaction}")


def main():
    """Run the Bank Management System."""

    while True:

        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                create_account()

            elif choice == 2:
                view_account()

            elif choice == 3:
                deposit_money()

            elif choice == 4:
                withdraw_money()

            elif choice == 5:
                check_balance()

            elif choice == 6:
                transaction_history()

            elif choice == 7:
                print("\nThank you for using Bank Management System.")
                break

            else:
                print("Please choose a number between 1 and 7.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
