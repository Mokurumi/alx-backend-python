#!/usr/bin/env python3
'''
Type-annotated function safely_get_value that takes a Mapping, Any,
and an optional argument in the form of a default value and returns
the value of the key. If the key doesn’t exist, the function should
return the default value.
'''


from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''
    Returns the value of a key in a dictionary
    '''
    if key in dct:
        return dct[key]
    else:
        return default
