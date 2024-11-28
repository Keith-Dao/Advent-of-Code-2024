"""
Day 12 solver.
"""

from pathlib import Path

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 12 solver.
    """

    def part_1(self, file: Path) -> int:
        return 1

    def part_2(self, file: Path) -> int:
        return 1


if __name__ == "__main__":
    solver = Solver()
    solver.solve("input.txt")
