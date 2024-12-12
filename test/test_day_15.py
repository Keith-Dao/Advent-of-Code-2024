"""
Tests day 15 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_15 import Solver


class TestDay15(BaseTests):
    """Tests the day 15 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
