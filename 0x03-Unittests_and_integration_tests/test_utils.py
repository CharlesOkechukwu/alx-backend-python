#!/usr/bin/env python3
"""module for the TestAccessNestedMap class"""
import unittest
from parameterized import parameterized
from typing import (Dict, Tuple, Union)
from unittest.mock import patch
from utils import access_nested_map


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
