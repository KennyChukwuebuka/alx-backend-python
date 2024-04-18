#!/usr/bin/env python3
"""Augment the following code with the
correct duck-typed annotations:
"""


from typing import Union, Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely returns the first element of the list
    if it exists, otherwise returns None.
    Args:
        lst (Sequence[Any]): The input list.
    Returns:
        Union[Any, None]: The first element of
        the list, if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
