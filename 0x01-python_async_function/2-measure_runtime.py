#!/usr/bin/env python3
"""
Module containing a function to measure the average execution time of wait_n.
"""

import asyncio
from typing import List
from time import perf_counter
from basic_async_syntax import wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the average execution time of wait_n(n, max_delay).

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay in seconds for each wait_random.
        Default is 10.

    Returns:
        float: The average execution time of wait_n in seconds.
    """
    total_elapsed_time = 0.0
    for _ in range(n):
        start_time = perf_counter()
        asyncio.run(wait_n(1, max_delay))
        end_time = perf_counter()
        total_elapsed_time += end_time - start_time
    return total_elapsed_time / n
