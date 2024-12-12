"""
Tests day 4 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_04 import Solver


class TestDay4(BaseTests):
    """Tests the day 4 solver."""

    solver = Solver()
    cases = [
        (
            """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""",
            18,
            9,
        )
    ]
