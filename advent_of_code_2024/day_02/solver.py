"""
Day 2 solver.
"""

from pathlib import Path
import sys
from typing import Generator

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 2 solver.
    """

    def _is_valid(self, nums: list[int], skip: int = -1) -> bool:
        """
        Checks if the sequence of numbers is valid.

        A sequence is valid if:
            - Every adjacent number is increasing or decreasing
            - The adjacent difference is in [1, 3]

        Args:
            nums: The sequence of numbers.
            skip: The index of the number of remove.

        Returns:
            True if the sequence is valid. Else, false.
        """

        def get_pairs_with_skip() -> Generator[tuple[int, int], None, None]:
            """
            Gets the number pairs accounting for the skip index.

            Yields:
                The adjacent numbers.
            """

            def get_next_index(index: int) -> int:
                """
                Gets the next index, accounting for the skip index.

                Args:
                    index: The index to get the next of.

                Returns:
                    The next index.
                """
                return (index := index + 1) + (index == skip)

            i = get_next_index(-1)
            j = get_next_index(i)

            while j < len(nums):
                yield nums[i], nums[j]
                i = j
                j = get_next_index(j)

        x, y = next(get_pairs_with_skip())
        increasing = x < y
        for x, y in get_pairs_with_skip():
            diff = y - x
            if not increasing:
                diff = -diff

            if not 1 <= diff <= 3:
                return False

        return True

    def part_1(self, filepath: Path) -> int:
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            return sum(
                self._is_valid([int(x) for x in line.split()]) for line in file
            )

    def part_2(self, filepath: Path) -> int:
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            return sum(
                (
                    self._is_valid(nums := [int(x) for x in line.split()])
                    or any(self._is_valid(nums, i) for i in range(len(nums)))
                )
                for line in file
            )
