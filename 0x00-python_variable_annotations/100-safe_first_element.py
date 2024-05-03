#!/usr/bin/env python3
"""module to annotate a duck-type function properly"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """accepts a sequence object and returns the value of the
    first element in the object or None if object is empty"""
    if lst:
        return lst[0]
    else:
        return None
