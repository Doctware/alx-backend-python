#!/usr/bin/env python3
""" this module anotate function """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of strings and returns a list of tuples.
    """
    return [(i, len(i)) for i in lst]
