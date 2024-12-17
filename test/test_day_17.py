"""
Tests day 17 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_17 import Solver


class TestDay17(BaseTests):
    """Tests the day 17 solver."""

    solver = Solver()
    cases = [
        (
            """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""",
            "4,6,3,5,6,3,5,2,1,0",
            29328,
        ),
        (
            """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""",
            "5,7,3,0",
            117440,
        ),
    ]
