import unittest
from P0_Function_variables.indoor_voice import indoor_voice
class TestYourFunction(unittest.TestCase):
    def test_lower_case(self):
        input_str = "HELLO"
        expected_output = "hello"
        self.assertEqual(indoor_voice(input_str), expected_output)

    def test_mixed_case(self):
        input_str = "HeLlO"
        expected_output = "hello"
        self.assertEqual(indoor_voice(input_str), expected_output)

    def test_empty_string(self):
        input_str = ""
        expected_output = ""
        self.assertEqual(indoor_voice(input_str), expected_output)

if __name__ == "__main__":
    unittest.main()