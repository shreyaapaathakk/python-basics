"""
Mini Project: Shopping List Manager

Concepts Used:
- Lists
- Loops
- Conditionals
- List methods
"""

shopping_list = []

while True:
    print("\n===== Shopping List Manager =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        shopping_list.append(item)
        print(f"{item} added successfully!")

    elif choice == "2":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed successfully!")
        else:
            print("Item not found.")

    elif choice == "3":
        print("\nShopping List")

        if shopping_list:
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        print("Thank you for using Shopping List Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
