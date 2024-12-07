"""
Tests day 7 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_07 import Solver


class TestDay7(BaseTests):
    """Tests the day 7 solver."""

    solver = Solver()
    example_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    part_1_solution = 3749
    part_2_solution = 11387
