class Currency:

    currencies =  {'CHF': 0.930023, # swiss franc 
                   'CAD': 1.264553, # canadian dollar
                   'GBP': 0.737414, # british pound
                   'JPY': 111.019919, # japanese yen
                   'EUR': 0.862361, # euro
                   'USD': 1.0} # us dollar

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        An Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __repr__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, Currency):
            # Convert the other currency to the unit of self
            other_value_in_self_unit = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
            return Currency(self.value + other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            # Treat other as USD value
            other_value_in_self_unit = other / Currency.currencies["USD"] * Currency.currencies[self.unit]
            return Currency(self.value + other_value_in_self_unit, self.unit)
        else:
            return NotImplemented

    def __iadd__(self, other):
        result = self.__add__(other)
        self.value = result.value
        self.unit = result.unit
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Currency):
            # Convert the other currency to the unit of self
            other_value_in_self_unit = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
            return Currency(self.value - other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            # Treat other as USD value
            other_value_in_self_unit = other / Currency.currencies["USD"] * Currency.currencies[self.unit]
            return Currency(self.value - other_value_in_self_unit, self.unit)
        else:
            return NotImplemented

    def __isub__(self, other):
        result = self.__sub__(other)
        self.value = result.value
        self.unit = result.unit
        return self

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            # Treat other as USD value
            other_value_in_usd = other
            other_value_in_self_unit = other_value_in_usd / Currency.currencies["USD"] * Currency.currencies[self.unit]
            return Currency(other_value_in_self_unit - self.value, self.unit)
        else:
            return NotImplemented

# Example usage
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)  # Currency in v1's unit (EUR)
print(v2 + v1)  # Currency in v2's unit (USD)
print(v1 + 3)   # Adding USD value to EUR
print(3 + v1)   # Adding USD value to EUR
print(v1 - 3)   # Subtracting USD value from EUR
print(30 - v2)  # Subtracting USD value from USD
