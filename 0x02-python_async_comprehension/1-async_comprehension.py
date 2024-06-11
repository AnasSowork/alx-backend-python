#!/usr/bin/env python3
"""
This module contains the coroutine async_comprehension which collects
random numbers from async_generator.
"""

import asyncio
from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [number async for number in async_generator()]
