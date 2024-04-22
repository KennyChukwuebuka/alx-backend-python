#!/usr/bin/env python3
"""Take the code from wait_n and alter it
into a new function task_wait_n. The code
is nearly identical to wait_n except
task_wait_random is being called.
"""


import asyncio
import random
from typing import List


async def wait_random(max_delay=10):
    """
    Asynchronously waits for a random delay
    between 0 and `max_delay` seconds, then returns the delay.

    Args:
        max_delay (int): The maximum delay
        in seconds. Defaults to 10.

    Returns:
        float: The delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task
    object that asynchronously waits for
    a random delay using the `wait_random` function.

    Parameters:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for `n` random delays
    each with a maximum delay of `max_delay`
    seconds, then returns a list of the delays.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay
        in seconds for each individual delay.

    Returns:
        List[float]: A list of floats
        representing the delays waited for.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
