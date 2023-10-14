#!/usr/bin/env python3
'''
Module: '5-sum_list'
Adds up the elements of a list
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns float after adding up elemens of a list'''
    sum: float = 0
    for item in input_list:
        sum += item

    return sum
