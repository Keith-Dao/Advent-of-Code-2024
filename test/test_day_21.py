"""
Tests day 21 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_21 import Solver


class TestDay21(BaseTests):
    """Tests the day 21 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
