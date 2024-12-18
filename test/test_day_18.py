"""
Tests day 18 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_18 import Solver


class TestDay18(BaseTests):
    """Tests the day 18 solver."""

    solver = Solver()
    cases = [
        (
            """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""",
            22,
            "6,1",
        )
    ]
    test_args = {"board_size": (7, 7), "limit": 12}
    ignore_args = ([], ["limit"])
