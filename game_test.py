""" game_test.py: This module defines tests with sample inputs to ensure
    functionality.
"""

import pytest
from gameboard import get_move


def test_board_range_1():
    """ Any move greater than [4,4] is outside of the 4 X 4 gameboard and
        should return False
    """
    assert get_move(5,1) == False


def test_board_range_2():
    """ Any move less than [1,1] is outside of the 4 X 4 gameboard and
        should return False
    """
    assert get_move(0,0) == False


def test_input_values():
    """ any non-numeric value should raise a value error.
    """
    with pytest.raises(ValueError, match='Values must be numeric.'):
        get_move('a','b')


