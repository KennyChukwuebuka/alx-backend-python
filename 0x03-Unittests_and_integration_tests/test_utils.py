#!/usr/bin/env python3
"""
Test utils.py
"""

import unittest
from parameterized import parameterized


def access_nested_map(data, keys, default=None):
    """
    Access nested values in a nested data structure using a sequence of keys.

    Args:
    - data (dict or list): The nested data structure
    (e.g., dictionary or list).
    - keys (iterable): A sequence of keys or indices
    to traverse the nested structure.
    - default (optional): The default value to return
    if the requested value is not found. Default is None.

    Returns:
    - The value found at the specified keys, or the default value if not found.
    """
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, IndexError, TypeError) as e:
        raise KeyError(f"Key not found: {keys}") from e


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map"""
    @parameterized.expand([
        ({}, ("a",), "Key not found: ('a',)"),
        ({"a": 1}, ("a", "b"), "Key not found: ('a', 'b')"),
    ])
    def test_access_nested_map_extension(self, nested_map, path,
                                         expected_error_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception.args[0]),
                         expected_error_message)


if __name__ == '__main__':
    unittest.main()
