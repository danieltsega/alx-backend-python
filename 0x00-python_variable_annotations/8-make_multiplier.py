#!/usr/bin/env python3
'''
Module: '8-make_multiplier'
Function that accepts a float multiplier and returns function
that multiplies a float by the multiplier
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returns function that multiplies a float by the multiplier
    '''

    def multiplier_function(value: float) -> float:
        '''Multiply float by the multiplier'''
        return value * multiplier

    return multiplier_function
