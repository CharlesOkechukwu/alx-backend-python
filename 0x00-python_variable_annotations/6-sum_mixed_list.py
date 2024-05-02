#!/usr/bin/env python3
"""pythopn module for mixed type function that adds the integer
and floats in a list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """accepts a mixed list of integers and floats and returns the
    sum of all list items in float"""
    return sum(mxd_list)
