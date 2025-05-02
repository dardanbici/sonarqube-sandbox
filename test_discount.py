import unittest
from good_pr import calculate_discount

class TestDiscountCalculation(unittest.TestCase):

    def test_valid_discount(self):
        self.assertEqual(calculate_discount(100, 20), 80.0)

    def test_zero_discount(self):
        self.assertEqual(calculate_discount(50, 0), 50.0)

    def test_full_discount(self):
        self.assertEqual(calculate_discount(100, 100), 0.0)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            calculate_discount(-10, 10)

    def test_invalid_discount_low(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, -5)

    def test_invalid_discount_high(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)

if __name__ == "__main__":
    unittest.main()
