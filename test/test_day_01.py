"""
Tests day 1 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_01 import Solver


class TestDay1(BaseTests):
    """Tests the day 1 solver."""

    solver = Solver()
    cases = [
        (
            """3   4
4   3
2   5
1   3
3   9
3   3""",
            11,
            31,
        )
    ]
