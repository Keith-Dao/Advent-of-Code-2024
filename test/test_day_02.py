"""
Tests day 2 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_02 import Solver


class TestDay2(BaseTests):
    """Tests the day 2 solver."""

    solver = Solver()
    example_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    part_1_solution = 2
    part_2_solution = 4
