"""
To-Do List Application

A beginner-friendly console application to manage daily tasks.

Features:
- Add tasks
- View tasks
- Mark tasks as completed
- Delete tasks

Author: Your Name
"""

tasks = []


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("              TO-DO LIST")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    """Add a new task."""

    task_name = input("\nEnter task: ").strip()

    if not task_name:
        print("Task cannot be empty.")
        return

    tasks.append(
        {
            "task": task_name,
            "completed": False
        }
    )

    print("Task added successfully.")


def view_tasks():
    """Display all tasks."""

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks")
    print("-" * 45)

    for index, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "✗ Pending"

        print(f"{index}. {task['task']}")
        print(f"   Status: {status}")
        print("-" * 45)


def mark_completed():
    """Mark a task as completed."""

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    """Delete a task."""

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"'{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Run the To-Do List application."""

    while True:
        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                add_task()

            elif choice == 2:
                view_tasks()

            elif choice == 3:
                mark_completed()

            elif choice == 4:
                delete_task()

            elif choice == 5:
                print("\nThank you for using the To-Do List application.")
                break

            else:
                print("Please choose a number between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
