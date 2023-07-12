import unittest
import config
from hamming import hamming

class HammingTestCase(unittest.TestCase):

    def test_hamming_distance(self):

        test_cases = [
            ("", "", 0),
            ("cat", "hat", 1),
            ("abc", "def", 3)
        ]

        for input_str1, input_str2, expected_output in test_cases:
            with self.subTest(input_str1=input_str1, input_str2=input_str2):
                self.assertEqual(hamming(input_str1, input_str2), expected_output)

    def test_non_string_arguments(self):

        test_cases = [
            (123, "abc", TypeError),
            ("abc", 123, TypeError)
        ]

        for arg1, arg2, expected_error in test_cases:
            with self.subTest(arg1=arg1, arg2=arg2):
                with self.assertRaises(expected_error):
                    hamming(arg1, arg2)

    def test_unequal_length_strings(self):

        with self.assertRaises(ValueError):
            hamming("abc", "defg")

if __name__ == '__main__':
    unittest.main()
