#!/usr/bin/env python3
'''
Module: '4-tasks'
Function that two args and returns a list of floating nums
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawns wait_random n times with the specified max_delay'''
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
