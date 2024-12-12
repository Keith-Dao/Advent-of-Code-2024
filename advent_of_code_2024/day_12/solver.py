"""
Day 12 solver.
"""

import itertools
from pathlib import Path
import sys
from typing import Callable

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 12 solver.
    """

    def _solve(
        self, filepath: Path, solve: Callable[[list[list[str]], int, int], int]
    ) -> int:
        board = []
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                board.append(list(line.strip()))
        m, n = len(board), len(board[0])

        return sum(solve(board, i, j) for i in range(m) for j in range(n))

    def part_1(self, filepath: Path) -> int:
        def solve(board: list[list[str]], start_i: int, start_j: int) -> int:
            """
            Solve for one group.

            Args:
                board: The input board.
                start_i: The starting row index.
                start_j: The starting column index.

            Returns:
                The solution for one group if it hasn't been visited
                before.
            """
            m, n = len(board), len(board[0])
            c = board[start_i][start_j]
            if c == "#":
                return 0

            stack = [(start_i, start_j)]
            perimeter = 0
            visited = set(stack)
            while stack:
                i, j = stack.pop()
                perimeter += 4

                for d_i, d_j in itertools.pairwise([0, 1, 0, -1, 0]):
                    n_i = i + d_i
                    n_j = j + d_j

                    if (
                        not 0 <= n_i < m
                        or not 0 <= n_j < n
                        or board[n_i][n_j] != c
                    ):
                        continue

                    perimeter -= 1
                    if (n_i, n_j) in visited:
                        continue

                    visited.add((n_i, n_j))
                    stack.append((n_i, n_j))

            for i, j in visited:
                board[i][j] = "#"

            return len(visited) * perimeter

        return self._solve(filepath, solve)

    def part_2(self, filepath: Path) -> int:
        def solve(board: list[list[str]], start_i: int, start_j: int) -> int:
            """
            Solve for one group.

            Args:
                board: The input board.
                start_i: The starting row index.
                start_j: The starting column index.

            Returns:
                The solution for one group if it hasn't been visited
                before.
            """
            m, n = len(board), len(board[0])
            c = board[start_i][start_j]
            if c == "#":
                return 0

            stack = [(start_i, start_j)]
            visited = set(stack)
            while stack:
                i, j = stack.pop()

                for d_i, d_j in itertools.pairwise([0, 1, 0, -1, 0]):
                    n_i = i + d_i
                    n_j = j + d_j

                    if (
                        not 0 <= n_i < m
                        or not 0 <= n_j < n
                        or board[n_i][n_j] != c
                    ):
                        continue

                    if (n_i, n_j) in visited:
                        continue

                    visited.add((n_i, n_j))
                    stack.append((n_i, n_j))

            def in_group(i: int, j: int, c: str) -> bool:
                """
                Check if the cell is in the group.

                Args:
                    i: Row index.
                    j: Column index.
                    c: The group.

                Returns:
                    True if in group, else false.
                """
                return 0 <= i < m and 0 <= j < n and board[i][j] == c

            perimeter = 0
            for i, j in visited:
                cell = [
                    in_group(i + d_i, j + d_j, c)
                    for d_i, d_j in [
                        (0, 1),
                        (1, 1),
                        (1, 0),
                        (1, -1),
                        (0, -1),
                        (-1, -1),
                        (-1, 0),
                        (-1, 1),
                    ]
                ]

                perimeter += sum(
                    # Outside corner
                    not (cell[k - 1] or cell[(k + 1) % len(cell)])
                    # Inside corner
                    or (
                        not cell[k]
                        and cell[k - 1]
                        and cell[(k + 1) % len(cell)]
                    )
                    for k in range(1, len(cell), 2)
                )

            for i, j in visited:
                board[i][j] = "#"
            return len(visited) * perimeter

        return self._solve(filepath, solve)
