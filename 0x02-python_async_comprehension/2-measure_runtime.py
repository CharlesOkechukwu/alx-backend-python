#!/usr/bin/env python3
"""module to measure runtime of asynchronous comprehension"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the runtime of 4  async comprehension function"""
    start: float = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end: float = time.time()
    return (end - start)
