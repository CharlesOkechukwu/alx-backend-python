#!/usr/bin/env python3
"""module for the TestAccessNestedMap class"""
import unittest
from parameterized import parameterized
from typing import (Dict, Tuple, Union)
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class that defines test methods for testing
    nested_map_access"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """test nested_map function in utils.py"""
        self.assertEqual(expected,
                         access_nested_map(nested_map, path))

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str]) -> None:
        """test if execption is correctly raised for nested_map function"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class that contains methods to test get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict[str, bool]
                      ) -> None:
        """test get_json that it returns the correct payload"""
        conf = {'return_value.json.return_value': test_payload}
        with patch('requests.get', autospec=True, **conf) as mock_req:
            self.assertEqual(get_json(test_url), test_payload)
            mock_req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """class that contains method to test for memoize function"""
    def test_memoize(self) -> None:
        """test for memoize function"""
        class TestClass:
            """memoize test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            self.assertEqual(test.a_property, mock.return_value)
            self.assertEqual(test.a_property, mock.return_value)
            mock.assert_called_once()
