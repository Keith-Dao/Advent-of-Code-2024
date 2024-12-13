"""
Tests day 13 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_13 import Solver


class TestDay13(BaseTests):
    """Tests the day 13 solver."""

    solver = Solver()
    cases = [
        (
            """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""",
            480,
            875318608908,
        )
    ]
