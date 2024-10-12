#!/usr/bin/env python3
""" this module contains a type-annotation function list as
    as an input of float then returns sum as float """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ this function takes list of float as args then
    returns sum of float """
    return sum(input_list)
