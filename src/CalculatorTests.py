import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data_add = CsvReader('/src/UnitTestAddition.csv').data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data_sub = CsvReader('/src/UnitTestSubtraction.csv').data
        for row in test_data_sub:
            self.assertEqual(self.calculator.sub(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication_method_calculator(self):
        test_data_multiplication = CsvReader('/src/UnitTestMultiplication.csv').data
        for row in test_data_multiplication:
            self.assertEqual(self.calculator.multiplication(int(row['Value 1']), int(row['Value 2'])),
                             int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_calculator(self):
        test_data_div = CsvReader('/src/UnitTestDivision.csv').data
        for row in test_data_div:
            self.assertEqual(self.calculator.div(float(row['Value 1']), float(row['Value 2'])),
                             float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_sqrt_method_calculator(self):
        test_data_sqrt = CsvReader('/src/UnitTestSquare Root.csv').data
        for row in test_data_sqrt:
            self.assertEqual(self.calculator.sqrt(float(row['Value 1'])), round(float(row['Result']), 8))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 8))

    def test_square_method_calculator(self):
        test_data_square = CsvReader('/src/UnitTestSquare.csv').data
        for row in test_data_square:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
