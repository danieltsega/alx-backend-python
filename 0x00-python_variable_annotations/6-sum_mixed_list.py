#!/usr/bin/env python3
'''
Module: '6-sum_mixed_list'
Adds up the elements of a list(int or float)
'''

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''Returns float after adding up elemens of a list(int or float)'''
    sum: float = 0
    for item in mxd_list:
        sum += item

    return sum
