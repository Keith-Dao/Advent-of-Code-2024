"""
Tests day 11 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_11 import Solver


class TestDay11(BaseTests):
    """Tests the day 11 solver."""

    solver = Solver()
    example_input = """125 17"""
    part_1_solution = 55312
    part_2_solution = 65601038650482
