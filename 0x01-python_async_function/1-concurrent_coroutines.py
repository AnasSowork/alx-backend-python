#!/usr/bin/env python3
"""
Module demonstrating concurrent execution of asyncio coroutines.
"""

import asyncio
from typing import List

# Import wait_random coroutine from previous file
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes the wait_random coroutine n times with specified max_delay.

    Args:
        n (int): Number of times to execute wait_random.
        max_delay (int): Maximum delay time for each execution of wait_random.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    # Use asyncio.gather to concurrently execute wait_random
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    # Sort the delays in ascending order
    sorted_delays = sorted(delays)

    return sorted_delays
