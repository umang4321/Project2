"""Subtraction Logic"""
from calculator.calculation import Calculation


class SubtractNumber(Calculation):
    """Getting subtraction of two numbers"""
    def getresult(self):
        """Subtraction method"""
        return self.value_a - self.value_b
