"""
Tests day 10 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_10 import Solver


class TestDay10(BaseTests):
    """Tests the day 10 solver."""

    solver = Solver()
    example_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    part_1_solution = 36
    part_2_solution = 81
