#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats and returns their sum as a float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats as input
    Args:
        mxd_lst (List[Union[int, float]]): The
        list of integers and floats to sum.
    Returns:
        float: The sum of the integers and
        floats in the input list.
    """
    return sum(mxd_lst)
