#/usr/bin/env bash
"""returns some of integers and float
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''returns the sum of list of ints and floating-point number
    '''
    return float(sum(mxd_list))
