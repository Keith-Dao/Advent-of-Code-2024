"""
Day 4 solver.
"""

import collections
import itertools
from pathlib import Path
import sys
from typing import Iterator

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 4 solver.
    """

    def get_last_character_position(
        self,
        filepath,
        word: str | Iterator[str],
        directions: list[int],
    ) -> dict[tuple[int, int, int, int], int]:
        """
        Get the number of paths to the last position of the search word.

        Args:
            filepath: The path to the input file.
            word: The word to search for.
            direction: The directions to search in.

        Returns:
            A mapping from the last positions to the number of
            paths with that last position.
        """
        word = iter(word)
        starting = next(word)
        positions = collections.defaultdict(int)
        graph = []
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for i, line in enumerate(file):
                for j, c in enumerate(line.strip()):
                    if c != starting:
                        continue

                    for direction in itertools.product(directions, repeat=2):
                        positions[(i, j, *direction)] += 1

                graph.append(line.strip())

        m, n = len(graph), len(graph[0])
        for c in word:
            next_ = collections.defaultdict(int)
            for (i, j, d_i, d_j), x in positions.items():
                n_i = i + d_i
                n_j = j + d_j

                if (
                    not 0 <= n_i < m
                    or not 0 <= n_j < n
                    or graph[n_i][n_j] != c
                ):
                    continue

                next_[(n_i, n_j, d_i, d_j)] += x
            positions = next_

        return positions

    def part_1(self, filepath: Path) -> int:
        return sum(
            self.get_last_character_position(
                filepath, "XMAS", [-1, 0, 1]
            ).values()
        )

    def part_2(self, filepath: Path) -> int:
        count = collections.defaultdict(int)
        for i, j, d_i, d_j in self.get_last_character_position(
            filepath, "MAS", [-1, 1]
        ):
            count[(i - d_i, j - d_j)] += 1

        return sum(x // 2 for x in count.values())
