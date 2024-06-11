#!/usr/bin/env python3

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values() -> None:
    """
    Collects values yielded by async_generator and prints them as a list.
    """
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    print(result)


if __name__ == "__main__":
    asyncio.run(print_yielded_values())
