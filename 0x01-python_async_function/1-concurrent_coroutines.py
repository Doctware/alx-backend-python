#!/usr/bin/env python3
""" this module implement cocurrent corouties """
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    this function implement cocurrent coroutines
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return delays
