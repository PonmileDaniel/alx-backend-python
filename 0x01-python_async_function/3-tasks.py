#!/usr/bin/env python3
"""
This module contain task_wait_randome function
"""


import asyncio


wait_n = __import__("0-basic_async_stntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
