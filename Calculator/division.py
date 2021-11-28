"""Division Logic"""

from calculator.calculation import Calculation


class DivideNumber(Calculation):
    """Getting division of two numbers"""
    def getresult(self):
        """Division method"""
        return self.value_a / self.value_b
