#!/usr/bin/env python3
"""
Test utils.py
"""

import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
import requests
from functools import wraps


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
    except (KeyError, IndexError, TypeError):
        return default


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


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
    except (KeyError, IndexError, TypeError) as e:
        raise KeyError(f"Key not found: {keys}") from e


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({}, ("a",), "Key not found: ('a',)"),
        ({"a": 1}, ("a", "b"), "Key not found: ('a', 'b')"),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_error_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected_error_message)


def get_json(url):
    """
    Get JSON data from a URL.

    Args:
    - url (str): The URL to fetch JSON data from.

    Returns:
    - dict: The JSON data.
    """
    response = requests.get(url)
    return response.json()


class TestGetJson(unittest.TestCase):
    """Test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json"""
        # Mocking the json method of the response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Calling the function under test
        result = get_json(test_url)

        # Asserting that requests.get was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)

        # Asserting that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


def memoize(func):
    """Memoize a function"""
    cache = {}

    @wraps(func)
    def memoizer(*args, **kwargs):
        """Memoizer wrapper"""
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return memoizer


class TestMemoize(unittest.TestCase):
    """Test memoize function"""
    class TestClass:
        def a_method(self):
            return 42

        @property
        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """Test memoize function"""
        with patch.object(self.TestClass, 'a_method',
                          return_value=42) as mock_method:
            instance = self.TestClass()
            result1 = instance.a_property
            result2 = instance.a_property

            # Assert that a_method is called only once
            mock_method.assert_called_once()

            # Assert that the correct result is returned
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
