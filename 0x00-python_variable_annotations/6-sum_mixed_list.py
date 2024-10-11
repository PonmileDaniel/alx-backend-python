#!/usr/bin/env python3

"""
    Annontation for Variable
    """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return float"""
    return float(sum(mxd_lst))
