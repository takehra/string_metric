import unittest
import config
from levenshtein import levenshtein_distance

class LevenshteinDistanceTests(unittest.TestCase):

    def test_same_strings(self):
        result = levenshtein_distance("hello", "hello")
        self.assertEqual(result, 0)

    def test_empty_strings(self):
        subtests = [
            ("", "", 0),
            ("hello", "", 5),
            ("", "world", 5)
        ]
        
        for s1, s2, expected in subtests:
            with self.subTest(s1=s1, s2=s2, expected=expected):
                result = levenshtein_distance(s1, s2)
                self.assertEqual(result, expected)

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
