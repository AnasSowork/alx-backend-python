#!/usr/bin/env python3
"""
Module containing a regular function to create asyncio.Task objects.
"""

import asyncio
from typing import Callable
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine \
        with the specified max_delay.

    Args:
        max_delay (int): The maximum delay time in seconds.

    Returns:
        asyncio.Task: The asyncio.Task object associated with wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
