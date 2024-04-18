#!/usr/bin/env python3
"""function that takes a list and returns a tuple with
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
