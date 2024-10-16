#!/usr/bin/env python3
""" this module contains a coroutines thats measure runtime """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    this corutines measure the runtime od the given corutines
    """
    start = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()

    total_time = end - start

    return total_time
