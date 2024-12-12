"""
Tests day 25 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_25 import Solver


class TestDay25(BaseTests):
    """Tests the day 25 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
