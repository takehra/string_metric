import unittest
import config
from hamming import hamming

class HammingTestCase(unittest.TestCase):
    def test_hamming_distance(self):
        self.assertEqual(hamming("cat", "hat"), 1)
        self.assertEqual(hamming("", ""), 0)

    def test_non_string_arguments(self):
        with self.assertRaises(TypeError):
            hamming(123, "abc")
        with self.assertRaises(TypeError):
            hamming("abc", 123)

    def test_unequal_length_strings(self):
        with self.assertRaises(ValueError):
            hamming("abc", "defg")

if __name__ == '__main__':
    unittest.main()
