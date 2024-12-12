"""
Tests day 22 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_22 import Solver


class TestDay22(BaseTests):
    """Tests the day 22 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
