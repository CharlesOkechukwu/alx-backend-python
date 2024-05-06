#!/usr/bin/env python3
"""module for async function to delay for a random
number of times"""
import asyncio
import random


async def wait_random(max_delay: int) -> int:
    """wait for a random amount of time not greater than max_delay"""
    wait: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
