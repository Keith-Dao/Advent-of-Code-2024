"""
Tests day 23 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_23 import Solver


class TestDay23(BaseTests):
    """Tests the day 23 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
