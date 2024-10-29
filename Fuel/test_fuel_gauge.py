import unittest
from fuel_gauge import consume

class TestFuelGauge(unittest.TestCase):
    def test_consume_valid_fraction(self):
        self.assertEqual(consume("1/4"), "25%")
        self.assertEqual(consume("1/2"), "50%")
        self.assertEqual(consume("3/4"), "75%")

    def test_consume_empty(self):
        self.assertEqual(consume("0/100"), "E")

    def test_consume_full(self):
        self.assertEqual(consume("100/100"), "F")

    def test_consume_invalid_fraction(self):
        self.assertFalse(consume("a/b"))
        self.assertFalse(consume("1/0"))
        
    def test_consume_non_integer(self):
        self.assertFalse(consume("1.5/4"))
        self.assertFalse(consume("1/4.5"))

if __name__ == "__main__":
    unittest.main()