#!/usr/bin/env python3
"""
Module containing a coroutine that collects 10 random
numbers using async comprehension.
"""

import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension
    over async_generator.

    Returns:
        List[float]: List of 10 random numbers.
    """
    random_numbers: List[float] = [num async for num in async_generator()]
    return random_numbers
