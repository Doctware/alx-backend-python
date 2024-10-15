#!/usr/bin/env python3
""" this module contains coroutines i.e a generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    this coroutines loops 10 times
    each time asyncronous wait 1sec the yield a random number
    bitween 0 - 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
