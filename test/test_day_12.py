"""
Tests day 12 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_12 import Solver


class TestDay12(BaseTests):
    """Tests the day 12 solver."""

    solver = Solver()
    example_input = """AAAA
BBCD
BBCC
EEEC"""
    part_1_solution = 140
    part_2_solution = 80
