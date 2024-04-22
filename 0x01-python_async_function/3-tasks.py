#!/usr/bin/env python3
"""Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer max_delay and
returns a asyncio.Task.
"""


import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronously waits for a random delay between 0 and max_delay seconds,
    then returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a task that waits for a random delay and returns the task.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created task.
    """
    return asyncio.create_task(wait_random(max_delay))
