#!/usr/bin/env python3
"""Async
"""


import asyncio
from typing import List
import random


async def wait_random(max_delay=10):
    """Asynchronously waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously waits for a random delay"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
