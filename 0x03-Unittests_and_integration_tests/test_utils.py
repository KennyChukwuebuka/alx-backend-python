#!/usr/bin/env python3
"""
Test utils.py
"""

import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function with various
        nested maps and paths.

        Parameters:
            nested_map (dict): The nested map to access.
            path (tuple): The path to the value in the nested map.
            expected (Any): The expected value at the given path.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
