#!/usr/bin/env python3
'''
Moule: '101-safely_get_value'
Return some key values or a given default
'''

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    '''Return some key values or a given default'''
    if key in dct:
        return dct[key]
    else:
        return default
