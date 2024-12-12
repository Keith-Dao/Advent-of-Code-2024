"""
Tests day 16 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_16 import Solver


class TestDay16(BaseTests):
    """Tests the day 16 solver."""

    solver = Solver()
    cases = [("""###""", -1, -1)]
