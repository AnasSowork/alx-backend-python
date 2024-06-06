#!/usr/bin/env python3
"""
This module provides a function to safely get the first element of a sequence.
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely get the first element of a sequence.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
