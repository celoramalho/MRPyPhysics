class Isu: #conversion unit to International System of Units
    def __init__(self):
        pass

class Isu:  # Conversion unit to International System of Units
    def __init__(self):
        pass

    # Length
    def millimeters(self, value):
        return value / 1000  # Convert to meters

    def centimeters(self, value):
        return value / 100  # Convert to meters

    def decimeters(self, value):
        return value / 10  # Convert to meters

    def meters(self, value):
        return value  # Already in meters

    def decameters(self, value):
        return value * 10  # Convert to meters

    def hectometers(self, value):
        return value * 100  # Convert to meters

    def kilometers(self, value):
        return value * 1000  # Convert to meters

    def inches(self, value):
        return value * 0.0254  # Convert to meters

    def feet(self, value):
        return value * 0.3048  # Convert to meters

    def yards(self, value):
        return value * 0.9144  # Convert to meters

    def miles(self, value):
        return value * 1609.34  # Convert to meters

    def nautical_miles(self, value):
        return value * 1852  # Convert to meters

    # Time
    def seconds(self, value):
        return value  # Already in seconds

    def milliseconds(self, value):
        return value / 1000  # Convert to seconds

    def microseconds(self, value):
        return value / 1e6  # Convert to seconds

    def nanoseconds(self, value):
        return value / 1e9  # Convert to seconds

    def minutes(self, value):
        return value * 60  # Convert to seconds

    def hours(self, value):
        return value * 3600  # Convert to seconds

    def days(self, value):
        return value * 86400  # Convert to seconds

    def weeks(self, value):
        return value * 604800  # Convert to seconds

    def months(self, value):
        return value * 2592000  # Approximation: 30 days

    def years(self, value):
        return value * 31536000  # Approximation: 365 days

    def decades(self, value):
        return value * 315567360  # Approximation: 10 years

    def centuries(self, value):
        return value * 3155673600  # Approximation: 100 years

    # Area
    def square_meters(self, value):
        return value  # Already in square meters

    def square_centimeters(self, value):
        return value / 10000  # Convert to square meters

    def square_millimeters(self, value):
        return value / 1e6  # Convert to square meters

    def square_kilometers(self, value):
        return value * 1e6  # Convert to square meters

    def hectares(self, value):
        return value * 10000  # Convert to square meters

    def acres(self, value):
        return value * 4046.86  # Convert to square meters

    def square_inches(self, value):
        return value * 0.00064516  # Convert to square meters

    def square_feet(self, value):
        return value * 0.092903  # Convert to square meters

    def square_yards(self, value):
        return value * 0.836127  # Convert to square meters

    def square_miles(self, value):
        return value * 2.59e6  # Convert to square meters

    # Speed
    def meters_per_second(self, value):
        return value  # Already in meters per second

    def kilometers_per_hour(self, value):
        return value / 3.6  # Convert to meters per second

    def miles_per_hour(self, value):
        return value * 0.44704  # Convert to meters per second

    def feet_per_second(self, value):
        return value * 0.3048  # Convert to meters per second

    def knots(self, value):
        return value * 0.514444  # Convert to meters per second

    # Acceleration
    def meters_per_second_squared(self, value):
        return value  # Already in m/s²

    def feet_per_second_squared(self, value):
        return value * 0.3048  # Convert to m/s²

    def g_force(self, value):
        return value * 9.80665  # Convert to m/s²

    # Mass
    def milligrams(self, value):
        return value / 1e6  # Convert to kilograms

    def grams(self, value):
        return value / 1000  # Convert to kilograms

    def kilograms(self, value):
        return value  # Already in kilograms

    def micrograms(self, value):
        return value / 1e9  # Convert to kilograms

    def tonnes(self, value):
        return value * 1000  # Convert to kilograms

    def pounds(self, value):
        return value * 0.453592  # Convert to kilograms

    def ounces(self, value):
        return value * 0.0283495  # Convert to kilograms

    def stone(self, value):
        return value * 6.35029  # Convert to kilograms

    def short_tons(self, value):
        return value * 907.184  # Convert to kilograms

    def long_tons(self, value):
        return value * 1016.05  # Convert to kilograms
