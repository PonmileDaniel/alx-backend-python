#!/usr/bin/env python3

"""
    Annontation for Variable
    """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(value: float) -> float:
        """Return that return func"""
        return multiplier * value

    """Return sum of two float"""
    return multiply
