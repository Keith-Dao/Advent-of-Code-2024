"""
Tests day 9 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_09 import Solver


class TestDay9(BaseTests):
    """Tests the day 9 solver."""

    solver = Solver()
    cases = [("""2333133121414131402""", 1928, 2858)]
