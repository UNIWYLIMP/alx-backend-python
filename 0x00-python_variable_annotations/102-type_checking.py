#!/usr/bin/python3
from typing import List, Tuple
"""Use  mypy to validate zoom_array function."""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return the zoomed value."""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)