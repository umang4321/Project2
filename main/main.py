""" This is the increment function"""
from calculator.addition import AddNumber
from calculator.subtraction import SubtractNumber
from calculator.multiplication import MultiplyNumber
from calculator.division import DivideNumber


class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def get_first_calculation():
        """First Calculation"""
        return Calculator.history[0].getresult()

    @staticmethod
    def clear_history():
        """Clear History"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """History count"""
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """Add calculation to history"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_last_calculation():
        """Last calculation"""
        return Calculator.history[-1].getresult()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        addition = AddNumber.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_calculation()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = SubtractNumber.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_calculation()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(MultiplyNumber.create(value_a, value_b))
        return Calculator.get_last_calculation()

    @staticmethod
    def division_numbers(value_a, value_b):
        """ divide two numbers and store the result"""
        Calculator.add_calculation_to_history(DivideNumber.create(value_a, value_b))
        return Calculator.get_last_calculation()
