"""Logic for calculator"""


class Calculation:
    """Calculation class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """Creating Calculation"""
        return cls(value_a, value_b)
