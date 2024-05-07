#!/usr/bin/env python3
"""module to measure the runtime of the async function wait_n"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure and return the total number of runtime of coroutine
    wait_n"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
