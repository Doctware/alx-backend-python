#!/usr/bin/env python3
""" complex sum """
from typing import Union, Tuple



def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    complex type-annotation
    """
    return (k, float(v ** 2))
