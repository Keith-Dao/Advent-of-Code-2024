"""
Tests day 4 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_04 import Solver


class TestDay4(BaseTests):
    """Tests the day 4 solver."""

    solver = Solver()
    example_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    part_1_solution = 18
    part_2_solution = 9
