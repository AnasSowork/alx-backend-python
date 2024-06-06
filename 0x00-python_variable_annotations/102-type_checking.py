#!/usr/bin/env python3
"""
This module provides a function to zoom an array by a given factor.
"""

from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on an array by repeating its elements a specified number of times.

    Args:
        lst (Tuple[int, ...]): The tuple of integers to zoom.
        factor (int, optional): The factor by which to zoom. Defaults to 2.

    Returns:
        List[int]: A list with the zoomed elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
