"""
Properties

This script demonstrates the property decorator.
"""


class Temperature:
    """Represents temperature."""

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")

        self._celsius = value


temperature = Temperature(25)

print(temperature.celsius)

temperature.celsius = 30

print(temperature.celsius)
