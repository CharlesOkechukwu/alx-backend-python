#!/usr/bin/env python3
"""python module for function that adds floats in a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """accepts list argument of floats and returns sums of
    all floats in the list"""
    add = 0.0
    for f in input_list:
        add += f
    return add
