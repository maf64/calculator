import unittest
import math
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_addition(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 1), 2)

    def test_subtraction(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(1, 1), 0)

    def test_multiplication(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(1, 1), 1)

    def test_division(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(1, 1), 1)

    def test_squaring(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(1, 1), 1)

    def test_squarerooting(self):
        calculator = Calculator()
        self.assertEqual(calculator.squareroot(1), 1)

    def test_results_property(self):
        calculator = Calculator()
        calculator.add(2, 1)
        self.assertEqual(calculator.result, 3)


if __name__ == '__main__':
    unittest.main()
