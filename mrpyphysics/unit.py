class Unit():
    units = (
    # Distance
    "meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles", "nautical miles",

    # Time
    "seconds", "milliseconds", "microseconds", "nanoseconds", "minutes", "hours", "days", "weeks", "months", "years",

    # Area
    "square meters", "square kilometers", "square centimeters", "square millimeters", 
    "hectares", "acres", "square inches", "square feet", "square yards", "square miles",

    # Speed
    "meters per second", "kilometers per hour", "miles per hour", 
    "feet per second", "knots",

    # Acceleration
    "meters per second squared", "feet per second squared", "g-force",

    # Mass
    "grams", "kilograms", "milligrams", "micrograms", "tonnes", 
    "pounds", "ounces", "stone", "short tons", "long tons"
)
    def __init__(self, value, unit):
        self.value = value 
        self.unit = unit
    
    def __str__(self):
        return f"{self.value} {self.unit}"