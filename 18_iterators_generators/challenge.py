"""
Challenge Project

Lazy File Reader

Objective:
Read a text file one line at a time using a generator.
"""


def read_file(file_name):
    """Yield one line at a time from a text file."""
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def main():
    """Run the Lazy File Reader application."""
    file_name = input("Enter file name: ")

    try:
        for line_number, line in enumerate(read_file(file_name), start=1):
            print(f"{line_number}: {line}")
    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()
