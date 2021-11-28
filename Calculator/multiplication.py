"""Multiplication logic"""

from calculator.calculation import Calculation


class MultiplyNumber(Calculation):
    """Getting multiplication of two numbers"""
    def getresult(self):
        """Multiplication method"""
        return self.value_a * self.value_b
