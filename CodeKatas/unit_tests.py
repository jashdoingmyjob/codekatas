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

    def test_return_six_when_add_one_two_three_with_newline_comma(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_return_sum_when_adding_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4,5"), 15)
    def test_return_sum_when_using_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)


if __name__ == '__main__':
    unittest.main()

# #python package: unittest
# def empty_string_test():
#     print(add(""))
# def more_than_three():
#     print(add("1,2,3,4,5"))
# def one_number():
#     print(add("1"))
# def two_numbers():
#     print(add("1, 2"))
# if __name__ == '__main__':
#     #empty_string_test()
#     #one_number()
#     #two_numbers()
