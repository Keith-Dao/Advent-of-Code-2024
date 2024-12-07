"""
Day 7 solver.
"""

import math
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 7 solver.
    """

    def _check(self, nums, target, check_concat=False) -> bool:
        """
        Checks if a sequence of numbers to can result in target.

        Args:
            num: The sequence of nums in order.
            target: The target value to reach.
            check_concat: Check if the concatenation operator can be used.

        Returns:
            True if the sequence can reach target, else false.
        """
        queue = {target}

        for x in reversed(nums):
            new_queue = set()
            for total in queue:
                if total == 0:
                    continue

                if total - x >= 0:
                    new_queue.add(total - x)

                if total % x == 0:
                    new_queue.add(total // x)

                if (
                    check_concat
                    and total % (tens := 10 ** (int(math.log10(x)) + 1)) == x
                ):
                    new_queue.add(total // tens)

            queue = new_queue

        return 0 in queue

    def _solve(self, filepath: Path, is_part_two: bool = False) -> int:
        """
        Solves the part.

        Args:
            filepath: The path to the file input.
            is_part_two: True if solving for part two, else false.

        Returns:
            The solution to the part.
        """
        result = 0
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                total, nums = line.strip().split(":")
                total = int(total)
                nums = [int(x) for x in nums.strip().split()]
                if self._check(nums, total, is_part_two):
                    result += total

        return result

    def part_1(self, filepath: Path) -> int:
        return self._solve(filepath, False)

    def part_2(self, filepath: Path) -> int:
        return self._solve(filepath, True)
