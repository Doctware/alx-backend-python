#!
""" this module contains a corutines thats implement comprehesion """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehesion() -> List[float]:
    """
    this corutines collecnt random number using an async comprehesion
    over async_generator then return the 10 random nuber
    """
    random_n = [i async for i in async_generator()]
    return random_n
