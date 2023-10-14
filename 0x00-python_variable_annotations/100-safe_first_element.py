#!/usr/bin/env python3
'''
Module: '100-safe_first_element'
Duck-typed annotated function
'''

from typing import List, Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of a list or None'''
    if lst:
        return lst[0]
    else:
        return None
