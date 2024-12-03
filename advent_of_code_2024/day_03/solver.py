"""
Day 3 solver.
"""

from pathlib import Path
import re
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 3 solver.
    """

    def part_1(self, filepath: Path) -> int:
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            return sum(
                int(x) * int(y)
                for line in file
                for x, y in re.findall(r"mul\((\d+),(\d+)\)", line)
            )

    def part_2(self, filepath: Path) -> int:
        result = 0
        enabled = True
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                for action, x, y in re.findall(
                    r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", line
                ):
                    if action == "don't()":
                        enabled = False
                    elif action == "do()":
                        enabled = True

                    if not action.startswith("mul") or not enabled:
                        continue

                    result += int(x) * int(y)

        return result


if __name__ == "__main__":
    solver = Solver()
    solver.solve("input.txt")
