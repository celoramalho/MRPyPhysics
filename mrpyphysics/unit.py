class Unit():
    conversion_factors = {
            # Distance (conversion to meters)
            "mm": 1e-3,
            "cm": 1e-2,
            "m": 1,
            "km": 1e3,
            "in": 0.0254,
            "ft": 0.3048,
            "yd": 0.9144,
            "mi": 1609.34,
            "nmi": 1852,

            # Time (conversion to seconds)
            "ms": 1e-3,
            "µs": 1e-6,
            "ns": 1e-9,
            "s": 1,
            "min": 60,
            "h": 3600,
            "d": 86400,
            "wk": 604800,
            "mo": 2592000,  # Approximation: 30 days
            "yr": 31536000,  # Approximation: 365 days

            # Area (conversion to square meters)
            "mm²": 1e-6,
            "cm²": 1e-4,
            "m²": 1,
            "km²": 1e6,
            "ha": 1e4,
            "ac": 4046.86,
            "in²": 6.4516e-4,
            "ft²": 0.092903,
            "yd²": 0.836127,
            "mi²": 2.59e6,

            # Speed (conversion to meters per second)
            "m/s": 1,
            "km/h": 1 / 3.6,
            "mph": 0.44704,
            "ft/s": 0.3048,
            "kn": 0.514444,

            # Acceleration (conversion to meters per second squared)
            "m/s²": 1,
            "ft/s²": 0.3048,
            "g": 9.80665,

            # Mass (conversion to kilograms)
            "µg": 1e-9,
            "mg": 1e-6,
            "g": 1e-3,
            "kg": 1,
            "t": 1e3,
            "lb": 0.453592,
            "oz": 0.0283495,
            "st": 6.35029,  # Stone
            "st": 907.184,  # Short tons (ambiguous, considere diferenciá-los)
            "lt": 1016.05,  # Long tons
    }
    def __init__(self, value: float | int, unit: str):
        if unit not in Unit.conversion_factors:
            raise ValueError(f"Invalid unit: {unit}")
        self.value = value 
        self.unit = unit
    
    def __str__(self):
        return f"{self.value} {self.unit}"
    
    def to_si(self):
        """
        Converte um valor para o Sistema Internacional de Unidades (SI).

        Args:
            value (float): O valor a ser convertido.
            unit (str): A unidade do valor.

        Returns:
            float: O valor convertido para SI.

        Raises:
            ValueError: Se a unidade não for reconhecida.
        """
        if self.unit not in Unit.conversion_factors:
            raise ValueError(f"Unidade '{self.unit}' não é válida ou suportada.")
        
        # Realiza a conversão
        return self.value * Unit.conversion_factors[self.unit]

    def to_unit (self, to_unit):
        value_si = self.to_si()
        value = value_si /Unit.conversion_factors[to_unit]
        return value
    
    @classmethod
    def valid_units(cls):
        return tuple(Unit.conversion_factors.keys())