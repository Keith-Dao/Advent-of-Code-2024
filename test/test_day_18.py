"""
Tests day 18 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_18 import Solver


class TestDay18(BaseTests):
    """Tests the day 18 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
