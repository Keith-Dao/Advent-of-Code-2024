"""
Tests day 14 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_14 import Solver


class TestDay14(BaseTests):
    """Tests the day 14 solver."""

    solver = Solver()
    cases = [
        (
            """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""",
            12,
            None,
        )
    ]

    test_args = {"size": (7, 11)}
