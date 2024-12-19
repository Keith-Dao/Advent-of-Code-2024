"""
Tests day 19 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_19 import Solver


class TestDay19(BaseTests):
    """Tests the day 19 solver."""

    solver = Solver()
    cases = [
        (
            """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""",
            6,
            16,
        )
    ]
