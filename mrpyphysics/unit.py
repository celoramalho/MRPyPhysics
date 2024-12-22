class Unit:
    conversion_factors = {
        # Distance (conversion to meters)
        "mm": 1e-3, "millimeters": 1e-3,
        "cm": 1e-2, "centimeters": 1e-2,
        "m": 1, "meters": 1,
        "km": 1e3, "kilometers": 1e3,
        "in": 0.0254, "inches": 0.0254,
        "ft": 0.3048, "feet": 0.3048,
        "yd": 0.9144, "yards": 0.9144,
        "mi": 1609.34, "miles": 1609.34,
        "nmi": 1852, "nautical_miles": 1852,

        # Time (conversion to seconds)
        "ms": 1e-3, "milliseconds": 1e-3,
        "µs": 1e-6, "microseconds": 1e-6,
        "ns": 1e-9, "nanoseconds": 1e-9,
        "s": 1, "seconds": 1,
        "min": 60, "minutes": 60,
        "h": 3600, "hours": 3600,
        "d": 86400, "days": 86400,
        "wk": 604800, "weeks": 604800,
        "mo": 2592000, "months": 2592000,  # Approximation: 30 days
        "yr": 31536000, "years": 31536000,  # Approximation: 365 days

        # Speed (conversion to meters per second)
        "m/s": 1, "meters_per_second": 1,
        "km/h": 1 / 3.6, "kilometers_per_hour": 1 / 3.6,
        "mph": 0.44704, "miles_per_hour": 0.44704,
        "ft/s": 0.3048, "feet_per_second": 0.3048,
        "kn": 0.514444, "knots": 0.514444,

        # Mass (conversion to kilograms)
        "µg": 1e-9, "micrograms": 1e-9,
        "mg": 1e-6, "milligrams": 1e-6,
        "g": 1e-3, "grams": 1e-3,
        "kg": 1, "kilograms": 1,
        "lb": 0.453592, "pounds": 0.453592,
        "oz": 0.0283495, "ounces": 0.0283495,
    }

    def __init__(self, value: float | int, unit: str):
        if unit not in Unit.conversion_factors:
            raise ValueError(f"Invalid unit: {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_si(self, return_as_object=True):
        """
        Convert the value to its equivalent in the SI unit.
        """
        value_si = self.value * Unit.conversion_factors[self.unit]
        return Unit(value_si, "SI") if return_as_object else value_si

    def to_unit(self, to_unit: str, return_as_object=True):
        """
        Convert the current unit to another unit.

        Args:
            to_unit (str): The target unit to convert to.
            return_as_object (bool): Whether to return a Unit object or just the value.

        Returns:
            Unit or float: The converted value.
        """
        if to_unit not in Unit.conversion_factors:
            raise ValueError(f"Invalid target unit: {to_unit}")
        
        value_si = self.to_si()
        converted_value = value_si / Unit.conversion_factors[to_unit]
        return Unit(converted_value, to_unit) if return_as_object else converted_value

    @classmethod
    def valid_units(cls):
        """
        Return all valid units available for conversion.
        """
        return tuple(cls.conversion_factors.keys())
    
    @classmethod
    def validate_and_convert_to_si(cls, *args):
        si_values = []
        for arg in args:
            if not isinstance(arg, Unit):
                raise TypeError(f"Expected Unit object, got {type(arg).__name__}")
            si_values.append(arg.to_si(return_as_object=False))
        return si_values
