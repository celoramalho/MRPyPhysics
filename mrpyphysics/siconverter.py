class SIConverter:
    def __init__(self):
        # Dicionário de fatores de conversão para unidades SI
        self.conversion_factors = {
            # Length (conversão para metros)
            "millimeters": 1e-3,
            "centimeters": 1e-2,
            "decimeters": 1e-1,
            "meters": 1,
            "decameters": 10,
            "hectometers": 1e2,
            "kilometers": 1e3,
            "inches": 0.0254,
            "feet": 0.3048,
            "yards": 0.9144,
            "miles": 1609.34,
            "nautical miles": 1852,

            # Time (conversão para segundos)
            "milliseconds": 1e-3,
            "microseconds": 1e-6,
            "nanoseconds": 1e-9,
            "seconds": 1,
            "minutes": 60,
            "hours": 3600,
            "days": 86400,
            "weeks": 604800,
            "months": 2592000,  # Aproximado: 30 dias
            "years": 31536000,  # Aproximado: 365 dias
            "decades": 315567360,  # Aproximado: 10 anos
            "centuries": 3155673600,  # Aproximado: 100 anos

            # Area (conversão para metros quadrados)
            "square millimeters": 1e-6,
            "square centimeters": 1e-4,
            "square meters": 1,
            "square kilometers": 1e6,
            "hectares": 1e4,
            "acres": 4046.86,
            "square inches": 6.4516e-4,
            "square feet": 0.092903,
            "square yards": 0.836127,
            "square miles": 2.59e6,

            # Speed (conversão para metros por segundo)
            "meters per second": 1,
            "kilometers per hour": 1 / 3.6,
            "miles per hour": 0.44704,
            "feet per second": 0.3048,
            "knots": 0.514444,

            # Acceleration (conversão para metros por segundo ao quadrado)
            "meters per second squared": 1,
            "feet per second squared": 0.3048,
            "g-force": 9.80665,

            # Mass (conversão para quilogramas)
            "micrograms": 1e-9,
            "milligrams": 1e-6,
            "grams": 1e-3,
            "kilograms": 1,
            "tonnes": 1e3,
            "pounds": 0.453592,
            "ounces": 0.0283495,
            "stone": 6.35029,
            "short tons": 907.184,
            "long tons": 1016.05,
        }

    def to_si(self, value, unit):
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
        if unit not in self.conversion_factors:
            raise ValueError(f"Unidade '{unit}' não é válida ou suportada.")
        
        # Realiza a conversão
        return value * self.conversion_factors[unit]

    def convert_unit (self, value, unit, to_unit):
        value_si = self.to_si(value, unit)
        value = value_si / self.conversion_factors[to_unit]
        return value
