#!/usr/bin/env python3
"""python module to multiply float by a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float and returns a functions that multiplies by a
    the multiplier"""
    def mul(n: float) -> float:
        """multiply float by float"""
        return multiplier * n
    return mul
