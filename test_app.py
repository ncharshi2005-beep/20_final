import unittest

class Calculator:
    def add(self, a, b):
        return a + b

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(10, 5), 15)

if __name__ == '__main__':
    unittest.main()
