#!/usr/bin/env python3
"""async coroutine comprehension module"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random nukbers using an async generator
    comprehension function"""
    return [i async for i in async_generator()]
