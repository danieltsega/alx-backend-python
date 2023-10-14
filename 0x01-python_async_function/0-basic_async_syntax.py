#!/usr/bin/env python3
'''
Module: '0-basic_async_syntax'
Asynchronous coroutine
'''

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''Returns random float between 0 and max_delay(included)'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
