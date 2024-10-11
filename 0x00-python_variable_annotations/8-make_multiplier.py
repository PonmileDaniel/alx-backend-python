#!/usr/bin/env python3

"""
    Annontation for Variable
    """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(value: float) -> float:
        return multiplier * value

    """Return sum of two float"""
    return multiply
