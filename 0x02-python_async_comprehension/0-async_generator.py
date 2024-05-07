#!/usr/bin/env python3
"""Module to create an async generator that loops 10 times"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """an async function that accepts no arguments and loops
    10 times each time wait 1 second asynchronously and returns a
    random number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
