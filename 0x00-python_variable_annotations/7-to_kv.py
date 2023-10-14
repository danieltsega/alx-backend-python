#!/usr/bin/env python3
'''
Module: '7-to_kv'
Accepts string and int/float then returns tuple of string & float
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns tuple of string and float'''
    return (k, v**2)
