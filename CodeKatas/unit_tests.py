#unit tests
import unittest

from stringcalculator import add


class TestStringMethods(unittest.TestCase):

    def test_return_zero_when_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_return_one_when_add_one(self):
        self.assertEqual(add("1"), 1)

    def test_return_three_when_add_one_two(self):
        self.assertEqual(add("1,2"), 3)

    def test_return_3_when_add_one_two_with_newline(self):
        self.assertEqual(add("1\n2"), 3)

    def test_return_sum_when_add_with_newline_comma(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_return_sum_when_adding_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4,5"), 15)

    def test_return_sum_when_using_semicolon_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_return_sum_when_using_minus_delimiter(self):
        self.assertEqual(add("//-\n1-2"), 3)

    def test_throw_exception_when_add_single_negative(self):
        with self.assertRaises(Exception): add("-1")
        
    def test_throw_exception_when_add_multiple_negatives(self):
        with self.assertRaises(Exception): add("1, -2, -5")


if __name__ == '__main__':
    unittest.main()
