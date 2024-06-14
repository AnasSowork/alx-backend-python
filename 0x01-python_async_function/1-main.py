#!/usr/bin/env python3

"""
Test file for printing the correct output of the wait_n coroutine.
"""


import asyncio
from concurrent_coroutines import wait_n


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
