"""
Tests day 14 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_14 import Solver


class TestDay14(BaseTests):
    """Tests the day 14 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
