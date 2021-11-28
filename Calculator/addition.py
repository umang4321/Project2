"""Addition Logic"""

from calculator.calculation import Calculation


class AddNumber(Calculation):
    """Defining Method for adding two numbers"""

    def getresult(self):
        """Addition method"""
        return self.value_a + self.value_b
