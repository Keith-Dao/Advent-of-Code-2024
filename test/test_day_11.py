"""
Tests day 11 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_11 import Solver


class TestDay11(BaseTests):
    """Tests the day 11 solver."""

    solver = Solver()
    cases = [("""125 17""", 55312, 65601038650482)]
