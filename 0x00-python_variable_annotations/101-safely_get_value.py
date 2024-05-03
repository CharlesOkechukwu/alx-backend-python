#!/usr/bin/env python3
"""module to return a value in a dictionary if key exists"""
from typing import Mapping, Any, Typevar, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] =
         None) -> Union[Any, T]:
    """accepts a dict, a key and a default argument and returns
    the value or None"""
    if key in dct:
        return dct[key]
    else:
        return default
