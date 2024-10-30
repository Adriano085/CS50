import unittest
from P0_Function_variables.making_faces import faces
class TestYourFunction(unittest.TestCase):
    def test_1(self):
        input_str = "Hello :)"
        expected_output = "Hello 🙂"
        self.assertEqual(faces(input_str), expected_output)

    def test_2(self):
        input_str = "Goodbye :("
        expected_output = "Goodbye 🙁"
        self.assertEqual(faces(input_str), expected_output)

    def test_3(self):
        input_str = "Hello :) Goodbye :("
        expected_output = "Hello 🙂 Goodbye 🙁"
        self.assertEqual(faces(input_str), expected_output)

if __name__ == "__main__":
    unittest.main()