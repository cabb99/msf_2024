# Start defining a simple add function

from typing import TypeVar
import numpy as np

Number = TypeVar('Number', int, float, np.number)

def add(a: Number, b: Number) -> Number:
    return a + b  # type: ignore

# Write a professional unit test for the add function

