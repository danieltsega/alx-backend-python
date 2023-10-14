#!/usr/bin/env python3
'''
Module: '1-async_comprehension'
Async Comprehension Function
'''

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Returns list of floating numbers'''
    results = [num async for num in async_generator()]
    return results
