#!/usr/bin/env python3
'''
Type-annotated function sum_mixed_list that takes a list mxd_lst of integers
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Returns the sum of a list of integers and floats
    '''
    return sum(mxd_lst)
