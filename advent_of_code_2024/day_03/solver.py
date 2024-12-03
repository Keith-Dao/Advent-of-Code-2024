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
                int(match[1]) * int(match[2])
                for line in file
                for match in re.finditer(r"mul\((\d+),(\d+)\)", line)
            )

    def part_2(self, filepath: Path) -> int:
        result = 0
        enabled = True
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                for match in re.finditer(
                    r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", line
                ):
                    if match.group(0) == "don't()":
                        enabled = False
                    elif match.group(0) == "do()":
                        enabled = True

                    if not match.group(0).startswith("mul") or not enabled:
                        continue

                    result += int(match.group(1)) * int(match.group(2))

        return result
