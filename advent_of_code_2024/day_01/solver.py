"""
Day 1 solver.
"""

import collections
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 1 solver.
    """

    def part_1(self, filepath: Path) -> int:
        left_nums, right_nums = [], []
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                nums = (int(x) for x in line.split())
                left_nums.append(next(nums))
                right_nums.append(next(nums))

        return sum(
            abs(x - y) for x, y in zip(sorted(left_nums), sorted(right_nums))
        )

    def part_2(self, filepath: Path) -> int:
        nums = []
        counter = collections.Counter()
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                line_nums = (int(x) for x in line.split())
                nums.append(next(line_nums))
                counter[next(line_nums)] += 1

        return sum(x * counter[x] for x in nums)


if __name__ == "__main__":
    solver = Solver()
    solver.solve("input.txt")
