import unittest
import config
from levenshtein import levenshtein_distance

class LevenshteinDistanceTests(unittest.TestCase):

    def test_same_strings(self):
        result = levenshtein_distance("hello", "hello")
        self.assertEqual(result, 0)

    def test_empty_string(self):
        result = levenshtein_distance("", "")
        self.assertEqual(result, 0)

    def test_insertion(self):
        result = levenshtein_distance("kitten", "sitting")
        self.assertEqual(result, 3)

    def test_deletion(self):
        result = levenshtein_distance("apple", "aple")
        self.assertEqual(result, 1)

    def test_substitution(self):
        result = levenshtein_distance("table", "label")
        self.assertEqual(result, 3)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            levenshtein_distance(123, "abc")

if __name__ == '__main__':
    unittest.main()
