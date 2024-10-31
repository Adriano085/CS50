import unittest
from P0_Function_variables.playback_speed import playback
class TestYourFunction(unittest.TestCase):
    def test_1(self):
        input_str = "This is CS50"
        expected_output = "This...is...CS50"
        self.assertEqual(playback(input_str), expected_output)

    def test_2(self):
        input_str = "This is our week on functions"
        expected_output = "This...is...our...week...on...functions"
        self.assertEqual(playback(input_str), expected_output)
        
    def test_3(self):
        input_str = "Let's implement a function called hello"
        expected_output = "Let's...implement...a...function...called...hello"
        self.assertEqual(playback(input_str), expected_output)

if __name__ == "__main__":
    unittest.main()