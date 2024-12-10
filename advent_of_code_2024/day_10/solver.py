"""
Day 10 solver.
"""

import collections
import itertools
from pathlib import Path
import sys
from typing import Generator

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 10 solver.
    """

    def _get_valid_highest_points_for_each_starting_point(
        self, filepath: Path
    ) -> Generator[dict[tuple[int, int], int], None, None]:
        """
        Starting for each starting point, yield the end points with a valid path.

        Args:
            filepath: The path to the input file.

        Yields:
            Mapping from end points to the number of unique paths that reaches that end
            point from the starting point.
        """
        positions = [set() for _ in range(10)]
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for i, line in enumerate(file):
                line = line.strip()
                for j, x in enumerate(line):
                    positions[int(x)].add((i, j))

        for i, j in positions[0]:
            queue = {(i, j): 1}
            for x in range(1, 10):
                new_queue = collections.defaultdict(int)
                for (i, j), count in queue.items():
                    for d_i, d_j in itertools.pairwise([0, 1, 0, -1, 0]):
                        if (i + d_i, j + d_j) in positions[x]:
                            new_queue[(i + d_i, j + d_j)] += count

                queue = new_queue
            yield queue

    def part_1(self, filepath: Path) -> int:
        return sum(
            len(queue)
            for queue in self._get_valid_highest_points_for_each_starting_point(
                filepath
            )
        )

    def part_2(self, filepath: Path) -> int:
        return sum(
            sum(queue.values())
            for queue in self._get_valid_highest_points_for_each_starting_point(
                filepath
            )
        )
