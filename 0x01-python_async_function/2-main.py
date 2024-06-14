#!/usr/bin/env python3

"""
Test file for measuring the runtime of wait_n coroutine.
"""

from measure_runtime import measure_time

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
