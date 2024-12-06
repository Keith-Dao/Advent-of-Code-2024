"""
Tests day 6 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_06 import Solver


class TestDay6(BaseTests):
    """Tests the day 6 solver."""

    solver = Solver()
    example_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    part_1_solution = 41
    part_2_solution = 6
