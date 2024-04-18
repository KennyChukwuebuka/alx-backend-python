#!/usr/bin/env python3
"""Use mypy to validate the following piece of
code and apply any necessary changes.
"""


from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in on an array by repeating each element multiple times.
    Args:
        lst (Tuple[int, ...]): The input tuple.
        factor (int, optional): The zoom factor. Defaults to 2.
    Returns:
        Tuple[int, ...]: The zoomed-in tuple.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
