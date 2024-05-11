#!/usr/bin/env python3
"""
Test utils.py
"""

import unittest
from parameterized import parameterized


def access_nested_map(data, keys, default=None):
    """
    Access nested values in a nested data structure
    using a sequence of keys.

    Args:
    - data (dict or list): The nested data structure
    (e.g., dictionary or list).
    - keys (iterable): A sequence of keys or indices to
    traverse the nested structure.
    - default (optional): The default value to return if
    the requested value is not found. Default is None.

    Returns:
    - The value found at the specified keys, or the default value if not found.
    """
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, IndexError, TypeError):
        return default


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
