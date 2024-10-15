#!/usr/bin/env python3
"""This module contains a coroutine that implements
asynchronous comprehension."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This coroutine collects 10 random numbers using an async comprehension
    over async_generator and returns them as a list.
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
