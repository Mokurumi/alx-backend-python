#!/usr/bin/env python3
'''
Type-annotated function element_length that takes a list lst of strings as
argument and returns a list of tuples, where each tuple contains a string and
its length.
'''


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Returns a list of tuples with a string and its length
    '''
    return [(i, len(i)) for i in lst]
