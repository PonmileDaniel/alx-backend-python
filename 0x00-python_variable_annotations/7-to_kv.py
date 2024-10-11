#!/usr/bin/env python3

"""
    Annontation for Variable
    """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """Return sum of two float"""
    return Tuple(k, float(v**2))
