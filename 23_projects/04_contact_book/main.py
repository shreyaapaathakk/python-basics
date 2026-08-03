"""
Contact Book

A beginner-friendly contact management system that allows users to
add, view, search, update, and delete contacts.

Author: Your Name
"""

contacts = []


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("        CONTACT BOOK")
    print("=" * 40)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def contact_exists(name):
    """
    Check if a contact exists.

    Args:
        name (str): Contact name.

    Returns:
        dict | None: Contact dictionary if found.
    """
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def add_contact():
    """Add a new contact."""

    print("\nAdd Contact")

    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if contact_exists(name):
        print("A contact with this name already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts.append(
        {
            "name": name,
            "phone": phone,
            "email": email
        }
    )

    print("Contact added successfully.")


def view_contacts():
    """Display all contacts."""

    if not contacts:
        print("\nNo contacts available.")
        return

    print("\nSaved Contacts")
    print("-" * 50)

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name : {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print("-" * 50)


def search_contact():
    """Search a contact by name."""

    if not contacts:
        print("\nNo contacts available.")
        return

    name = input("Enter contact name: ").strip()

    contact = contact_exists(name)

    if contact:
        print("\nContact Found")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")


def update_contact():
    """Update an existing contact."""

    if not contacts:
        print("\nNo contacts available.")
        return

    name = input("Enter contact name to update: ").strip()

    contact = contact_exists(name)

    if not contact:
        print("Contact not found.")
        return

    print("\nLeave a field blank to keep the current value.")

    new_phone = input(f"New phone ({contact['phone']}): ").strip()
    new_email = input(f"New email ({contact['email']}): ").strip()

    if new_phone:
        contact["phone"] = new_phone

    if new_email:
        contact["email"] = new_email

    print("Contact updated successfully.")


def delete_contact():
    """Delete a contact."""

    if not contacts:
        print("\nNo contacts available.")
        return

    name = input("Enter contact name to delete: ").strip()

    contact = contact_exists(name)

    if contact:
        contacts.remove(contact)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    """Run the Contact Book application."""

    while True:
        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                add_contact()

            elif choice == 2:
                view_contacts()

            elif choice == 3:
                search_contact()

            elif choice == 4:
                update_contact()

            elif choice == 5:
                delete_contact()

            elif choice == 6:
                print("\nThank you for using Contact Book.")
                break

            else:
                print("Please enter a number between 1 and 6.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
