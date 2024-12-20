"""
Day 20 solver.
"""

import collections
import itertools
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 20 solver.
    """

    def _solve(self, filepath: Path, limit: int, threshold: int = 100) -> int:
        """
        Solves a part.

        Args:
            filepath: The path to the input file.
            limit: The maximum number of steps that can be skipped.
            threshold: The minimum time savings.

        Returns:
            The solution to the part.
        """
        end = 0, 0
        board = []
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for i, line in enumerate(file):
                line = line.strip()
                board.append(line)
                for j, c in enumerate(line):
                    if c == "E":
                        end = i, j

        m, n = len(board), len(board[0])
        visited = [[-1] * n for _ in range(m)]
        visited[end[0]][end[1]] = 0
        queue = collections.deque([end])
        empty = []
        while queue:
            i, j = queue.popleft()
            empty.append((i, j))

            for d_i, d_j in itertools.pairwise([0, 1, 0, -1, 0]):
                next_node = n_i, n_j = i + d_i, j + d_j
                if board[n_i][n_j] == "#" or visited[n_i][n_j] != -1:
                    continue

                visited[n_i][n_j] = visited[i][j] + 1
                queue.append(next_node)

        result = 0
        for i, j in itertools.product(range(1, m - 1), range(1, n - 1)):
            if board[i][j] == "#":
                continue

            time = visited[i][j]
            for n_i in range(max(1, i - limit), min(m, i + limit + 1)):
                remaining_steps = limit - abs(i - n_i)
                for n_j in range(
                    max(1, j - remaining_steps),
                    min(n, j + remaining_steps + 1),
                ):
                    if visited[n_i][n_j] == -1:
                        continue

                    distance = abs(i - n_i) + abs(j - n_j)
                    if time - visited[n_i][n_j] - distance >= threshold:
                        result += 1

        return result

    def part_1(self, filepath: Path, threshold: int = 100) -> int:
        return self._solve(filepath, 2, threshold)

    def part_2(self, filepath: Path, threshold: int = 100) -> int:
        return self._solve(filepath, 20, threshold)
