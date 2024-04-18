#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats as input and returns their sum.
    Args:
        input_list (List[float]): The list of floats to sum.
    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
