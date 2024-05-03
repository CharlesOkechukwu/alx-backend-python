#!/usr/bin/env python3
"""python module that annotates a function"""
from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that accepts an iterable sequence and returns
    a list of Tuples"""
    return [(i, len(i)) for i in lst]
