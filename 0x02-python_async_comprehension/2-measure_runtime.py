#!/usr/bin/env python3
'''
Module: '2-measure_runtime'
Function that measures the runtime of an async comprehnsion function
'''

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Returns runtime of async_comprehension function'''
    start_time = time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return time() - start_time
