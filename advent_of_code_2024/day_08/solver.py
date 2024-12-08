"""
Day 8 solver.
"""

import collections
import itertools
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 8 solver.
    """

    def _solve(self, filepath: Path, is_part_two: bool = False) -> int:
        """
        Solves the part.

        Args:
            filepath: Path to input file.
            is_part_two: If true, solve for part two, else solve for part one.

        Returns:
            The solution to the part.
        """
        locations = collections.defaultdict(list)
        m = n = 0
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for i, line in enumerate(file):
                line = line.strip()
                for j, x in enumerate(line):
                    if x == ".":
                        continue

                    locations[x].append((i, j))

                n = len(line)
                m += 1

        result = set()
        for positions in locations.values():
            if is_part_two:
                result.update(positions)

            for (x_1, y_1), (x_2, y_2) in itertools.combinations(positions, 2):
                d_x = x_1 - x_2
                d_y = y_1 - y_2

                new_x, new_y = x_1 + d_x, y_1 + d_y
                while 0 <= new_x < m and 0 <= new_y < n:
                    result.add((new_x, new_y))
                    if not is_part_two:
                        break

                    new_x += d_x
                    new_y += d_y

                new_x, new_y = x_2 - d_x, y_2 - d_y
                while 0 <= new_x < m and 0 <= new_y < n:
                    result.add((new_x, new_y))
                    if not is_part_two:
                        break

                    new_x -= d_x
                    new_y -= d_y

        return len(result)

    def part_1(self, filepath: Path) -> int:
        return self._solve(filepath, False)

    def part_2(self, filepath: Path) -> int:
        return self._solve(filepath, True)
