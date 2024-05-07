#!/usr/bin/env python3
"""create a function task_wait_n that gathers the results from
task_wait_random"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """accepts arguments n and max_delay which are of type int
    and returns a list of floats"""
    wait = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))
    return sorted(wait)
