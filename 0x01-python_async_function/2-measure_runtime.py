#!/usr/bin/env python3
"""From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time
for wait_n(n, max_delay), and returns total_time / n.
Your function should return a float.

Use the time module to measure an
approximate elapsed time.
"""


import asyncio
import time
from typing import List
import random


async def wait_random(max_delay=10):
    """
    Asynchronously waits for a random delay between 0
    and `max_delay` seconds, then returns the delay.
    :param max_delay: The maximum delay in seconds. Defaults to 10.
    :type max_delay: int
    :return: The delay in seconds.
    :rtype: float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for `n` random delays each with a
    maximum delay of `max_delay` seconds,
    then returns a list of the delays.
    :param n: The number of random delays to wait for.
    :type n: int
    :param max_delay: The maximum delay in seconds for
    each individual delay.
    :type max_delay: int
    :return: A list of floats representing the delays waited for.
    :rtype: List[float]
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the execution time of the `wait_n`
    function with the given parameters.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay in seconds
        for each individual delay.

    Returns:
        float: The average time taken per delay in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
