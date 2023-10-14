#!/usr/bin/env python3
'''
Module: '9-element_length'
Returns a list of tuple of element of a list & it's length
'''

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples of elements and their length'''
    return [(i, len(i)) for i in lst]
