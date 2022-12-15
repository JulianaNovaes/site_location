import pytest
import numpy as np
from map import scale_map, multiply_array, combine_maps, update_plot


def test_multiply_array() -> None:
    """
    Checks if multiplication of arrays return the correct value. The arrays need to be converted to list to
    be compared
    """

    sample_array = np.array([[1, 2, 3], [1, 3, 4]])
    expected_array = np.array([[2, 4, 6], [2, 6, 8]])

    assert multiply_array(sample_array, 2).tolist() == expected_array.tolist()


def test_scale_map() -> None:
    """
    Checks if map is correctly scaled so that values are between 0-255
    """

    sample_array = np.array([[405, 123, 294], [43, -98, -7]])
    scaled_array = scale_map(sample_array)

    assert np.max(scaled_array) <= 255
    assert np.min(scaled_array) >= 0
