#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__("6-max_integer").max_integer
"""test the max_integer function"""


class TestMaxInt(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_no_argument(self):
        """Tests for function with no argument"""
        self.assertIsNone(max_integer([]))

    def test_empty_list(self):
        """test with empty list"""
        self.assertIsNone(max_integer())

    def test_with_normal_list(self):
        """ Tests with normal list"""
        result = max_integer([3, 5, 6, 7, 34, 99])
        self.assertEqual(result, 99)
        result = max_integer([3, 5])
        self.assertEqual(result, 5)
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_with_duplicate(self):
        """Tests with duplicate in the list"""
        result = max_integer([3, 5, 6, 7, 9, 9])
        self.assertEqual(result, 9)
        result = max_integer([34, 34, 34, 35])
        self.assertEqual(result, 35)

    def test_negative(self):
        """Tests using negative numbers"""
        result = max_integer([1, -1, 1, -3, -4, 0])
        self.assertEqual(result, 1)
        result = max_integer([0, -3, -4, -5])
        self. assertEqual(result, 0)
        result = max_integer([-3, -5, -5, -3, -2, -2, -1])
        self.assertEqual(result, -1)

    def test_none(self):
        """passing None as an argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_str(self):
        """Test with non int element in the list"""
        arr = ["hello", 4, 4, 3, 6, 6, 3432]
        with self.assertRaises(TypeError):
            max_integer(arr)


if __name__ == "__main__":
    unittest.main()
