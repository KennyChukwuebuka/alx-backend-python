#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier
that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.
    Args:
        multiplier (float): The multiplier to be used in the returned function.
    Returns:
        Callable[[float], float]: A function that
        multiplies a float by the given multiplier.
    """
    def multiply(value: float) -> float:
        """
        Multiplies a float by the given multiplier.
        Args:
            value (float): The float value to be multiplied.
        Returns:
            float: The result of multiplying the value by the multiplier.
        """
        return value * multiplier
    return multiply
