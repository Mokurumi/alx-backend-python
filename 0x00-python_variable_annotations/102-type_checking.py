#!/usr/bin/env python3
'''
Type-annotated function zoom_array that takes a Tuple input_tuple as argument
and an int factor and returns a list.
'''


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Returns a list of tuples with a string and its length
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
