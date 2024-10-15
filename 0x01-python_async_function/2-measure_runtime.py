#!/usr/bin/env python3
""" this module contains the function thats calculate the runtimr """
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    this finction measures the total execution time
    for the given concurrent coroutines
    """
    t: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    t = time.time() - t
    return t/n
