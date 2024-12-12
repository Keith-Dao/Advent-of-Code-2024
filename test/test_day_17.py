"""
Tests day 17 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_17 import Solver


class TestDay17(BaseTests):
    """Tests the day 17 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
