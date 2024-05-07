#!/usr/bin/env python3
"""module to create an asynchronous task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """accepts an integer argument max-delay which specifies max
    delay time and creates and return an asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
