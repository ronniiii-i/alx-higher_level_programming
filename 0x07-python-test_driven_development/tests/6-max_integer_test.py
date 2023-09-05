#!/usr/bin/python3
"""Unittests for max_integer([...])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer([...])"""

    def test_ordered_list(self):
        """Test and ordered list of int"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_unordered_list(self):
        """Test unordered list of int"""
        self.assertEqual(max_integer([1, 4, 5, 2, 6, 3]), 6)

    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_reversed_list(self):
        """Test reversed list of ints"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_single_element_list(self):
        """Test single element list of ints"""
        self.assertEqual(max_integer([8]), 8)

    def test_floats(self):
        """Test list of floats"""
        self.assertEqual(max_integer([12.8, 7.78, 4]), 12.8)

    def test_ints_and_floats(self):
        """Test  alist of ints and floats"""
        self.assertEqual(max_integer([1, 12.8, 7.78, 4]), 12.8)

    def test_string(self):
        """Test a string"""
        self.assertEqual(max_integer('Roni'), 'o')

    def test_list_of_strings(self):
        """Test a list of strings"""
        list_of_strings = ['A', 'list', 'of', 'multiple', 'strings']
        self.assertEqual(max_integer(list_of_strings), 'strings')

    def empty_string(self):
        """Test empty string"""
        self.assertEqual(max_integer(''), None)


if __name__ == '__main__':
    unittest.main()
