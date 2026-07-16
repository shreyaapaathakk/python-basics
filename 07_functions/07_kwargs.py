"""
Variable-Length Keyword Arguments
"""


def profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


profile(
    name="Shreya",
    age=22,
    language="Python"
)
