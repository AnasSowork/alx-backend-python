#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    """
    Main function to test measure_runtime.
    """
    runtime = await measure_runtime()
    print(runtime)

if __name__ == "__main__":
    asyncio.run(main())
