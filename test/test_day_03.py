"""
Tests day 3 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_03 import Solver


class TestDay3(BaseTests):
    """Tests the day 3 solver."""

    solver = Solver()
    part_1_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
    part_2_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    part_1_solution = 161
    part_2_solution = 48
