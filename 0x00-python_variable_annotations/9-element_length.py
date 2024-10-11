#!/usr/bin/env python3

"""
    Annontation for Variable
    """

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Take a float"""
    return [(i, len(i)) for i in lst]
