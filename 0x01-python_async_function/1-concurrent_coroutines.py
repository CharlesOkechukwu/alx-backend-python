#!/usr/bin/env python3
"""module for gathering concurrent routines for n number of times"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """accepts arguments n and max_delay which are of type int
    and returns a list of floats"""
    wait = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(wait)
