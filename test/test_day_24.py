"""
Tests day 24 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_24 import Solver


class TestDay24(BaseTests):
    """Tests the day 24 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
