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
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )
    end = time.time()

    total_time = end - start

    return total_time
