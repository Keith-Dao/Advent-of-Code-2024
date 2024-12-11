"""
Day 11 solver.
"""

import collections
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 11 solver.
    """

    def _solve(self, filepath: Path, times: int) -> int:
        """
        Solves the part.

        Args:
            filepath: The path to the file input.
            times: The number of times to run the simulation.

        Returns:
            The solution to the part.
        """
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            nums = file.read().strip().split()

        counts = {x: 1 for x in nums}
        for _ in range(times):
            new_counts = collections.defaultdict(int)
            for x, c in counts.items():
                if x == "0":
                    new_counts["1"] += c
                    continue

                if len(x) % 2 == 1:
                    new_counts[str(2024 * int(x))] += c
                    continue

                new_counts[x[: len(x) // 2]] += c
                new_counts[str(int(x[len(x) // 2 :]))] += c

            counts = new_counts

        return sum(counts.values())

    def part_1(self, filepath: Path) -> int:
        return self._solve(filepath, 25)

    def part_2(self, filepath: Path) -> int:
        return self._solve(filepath, 75)
