"""
Tests day 12 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_12 import Solver


class TestDay12(BaseTests):
    """Tests the day 12 solver."""

    solver = Solver()
    cases = [
        (
            """AAAA
BBCD
BBCC
EEEC""",
            140,
            80,
        ),
        (
            """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO""",
            772,
            436,
        ),
        (
            """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""",
            1930,
            1206,
        ),
        (
            """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""",
            692,
            236,
        ),
        (
            """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA""",
            1184,
            368,
        ),
    ]
