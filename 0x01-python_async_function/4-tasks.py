#!/usr/bin/env python3
"""
Module containing functions to create asyncio.Task objects
for concurrent coroutines.
"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def task_wait_random(max_delay: int) -> float:
    """
    Creates and runs the wait_random coroutine with the
    specified max_delay.

    Args:
        max_delay (int): The maximum delay time in seconds.

    Returns:
        float: The delay returned by wait_random.
    """
    return await wait_random(max_delay)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns
    the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds for each
        task_wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)  # Wait for all tasks
    return sorted(results)
