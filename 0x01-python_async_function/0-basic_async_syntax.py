#!/usr/bin/env python3
"""Module demonstrating an asynchronous coroutine that waits
for a random delay."""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns
    the delay.

    Args:
        max_delay (int): The maximum delay time in seconds. Default is 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
