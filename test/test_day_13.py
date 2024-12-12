"""
Tests day 13 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_13 import Solver


class TestDay13(BaseTests):
    """Tests the day 13 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
