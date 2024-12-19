class Unit():
    def __init__(self):
        self.valid_units = {
            # Distance
            "meters": "m",
            "kilometers": "km",
            "centimeters": "cm",
            "millimeters": "mm",
            "inches": "in",
            "feet": "ft",
            "yards": "yd",
            "miles": "mi",
            "nautical miles": "nmi",

            # Time
            "seconds": "s",
            "milliseconds": "ms",
            "microseconds": "µs",
            "nanoseconds": "ns",
            "minutes": "min",
            "hours": "h",
            "days": "d",
            "weeks": "wk",
            "months": "mo",
            "years": "yr",

            # Area
            "square meters": "m²",
            "square kilometers": "km²",
            "square centimeters": "cm²",
            "square millimeters": "mm²",
            "hectares": "ha",
            "acres": "ac",
            "square inches": "in²",
            "square feet": "ft²",
            "square yards": "yd²",
            "square miles": "mi²",

            # Speed
            "meters per second": "m/s",
            "kilometers per hour": "km/h",
            "miles per hour": "mph",
            "feet per second": "ft/s",
            "knots": "kn",

            # Acceleration
            "meters per second squared": "m/s²",
            "feet per second squared": "ft/s²",
            "g-force": "g",

            # Mass
            "grams": "g",
            "kilograms": "kg",
            "milligrams": "mg",
            "micrograms": "µg",
            "tonnes": "t",
            "pounds": "lb",
            "ounces": "oz",
            "stone": "st",
            "short tons": "st",
            "long tons": "lt"
        }

    def __init__(self, value, unit):
        if unit not in self.valid_units or unit not in self.valid_units.values():
            raise ValueError(f"Invalid unit: {unit}")
        self.value = value 
        self.unit = unit
    
    def __str__(self):
        return f"{self.value} {self.unit}"