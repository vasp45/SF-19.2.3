import pytest
from app.calculator import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_mul(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_div(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_sub(self):
        assert self.calc.subtraction(self, 3, 2) == 1

    def test_add(self):
        assert self.calc.adding(self, 2, 3) == 5
