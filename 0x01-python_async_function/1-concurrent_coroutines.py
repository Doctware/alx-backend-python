#!/usr/bin/env python3
""" this module implement cocurrent coroutines
    impoerting basic syntac from basic async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function implement cocurrent coroutines
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
