#!/usr/bin/env python3
"""python module for an annotated function that returns a tupule
with mixed value types"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """take two arguments a string and a tuple made up of integers
    and floats and return a tuple made up of first a string, then
    a float"""
    return k, v*v
