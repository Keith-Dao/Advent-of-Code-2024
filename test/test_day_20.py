"""
Tests day 20 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_20 import Solver


class TestDay20(BaseTests):
    """Tests the day 20 solver."""

    solver = Solver()
    cases = [
        (
            """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""",
            1,
            285,
        )
    ]
    test_args = {"threshold": 50}
