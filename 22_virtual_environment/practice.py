"""
practice.py

Solutions for Virtual Environment exercises.
"""

print("=" * 10, "Exercise 1", "=" * 10)
print("python -m venv venv")

print("\n" + "=" * 10, "Exercise 2", "=" * 10)
print(r"Windows (CMD): venv\Scripts\activate")
print(r"Windows (PowerShell): .\venv\Scripts\Activate.ps1")
print("macOS/Linux: source venv/bin/activate")

print("\n" + "=" * 10, "Exercise 3", "=" * 10)
print("pip install requests")

print("\n" + "=" * 10, "Exercise 4", "=" * 10)
print("pip install numpy")

print("\n" + "=" * 10, "Exercise 5", "=" * 10)
print("pip freeze > requirements.txt")

print("\n" + "=" * 10, "Exercise 6", "=" * 10)
print("pip install -r requirements.txt")

print("\n" + "=" * 10, "Exercise 7", "=" * 10)
print("deactivate")

print("\n" + "=" * 10, "Bonus Challenge", "=" * 10)

commands = [
    "python -m venv venv",
    r"venv\Scripts\activate",
    "pip install requests pandas",
    "pip freeze > requirements.txt",
    "pip install -r requirements.txt",
]

for command in commands:
    print(command)
