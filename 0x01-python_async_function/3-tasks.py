#!/usr/bin/env python3
'''
Module: '3-tasks'
Function that take an int and returns asyncio.Task
'''

import asyncio
from typing import Union
from functools import partial

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Returns asyncio.Task'''
    partial_wait_random = partial(wait_random, max_delay)
    task = asyncio.create_task(partial_wait_random())

    return task
