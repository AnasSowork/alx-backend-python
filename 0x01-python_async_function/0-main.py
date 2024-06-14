#!/usr/bin/env python3

"""
Main module to test the wait_random coroutine.
"""

import asyncio
from 0-basic_async_syntax import wait_random

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
