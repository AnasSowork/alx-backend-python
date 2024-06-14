#!/usr/bin/env python3
"""
Module to measure the runtime of wait_n function calls.
"""


import time
from typing import List
from asyncio import run

# Import wait_n function from previous file
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay time for each wait_n call.

    Returns:
        float: Average execution time per call of wait_n.
    """
    start_time = time.perf_counter()
    run(wait_n(n, max_delay))  # Run wait_n asynchronously and wait
    end_time = time.perf_counter()

    total_time = end_time - start_time
    avg_time_per_call = total_time / n

    return avg_time_per_call


# Example usage
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
