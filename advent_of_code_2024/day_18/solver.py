"""
Day 18 solver.
"""

import collections
import itertools
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 18 solver.
    """

    def part_1(
        self,
        filepath: Path,
        board_size: tuple[int, int] = (71, 71),
        limit: int = 1024,
    ) -> int:
        blocked = set()
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line_num, line in enumerate(file):
                if line_num == limit:
                    break

                j, i = line.strip().split(",")
                blocked.add((int(i), int(j)))

        m, n = board_size
        queue = collections.deque([(0, 0)])
        visited = set(queue)
        steps = 0
        while queue:
            steps += 1

            for _ in range(len(queue)):
                i, j = queue.popleft()
                for d_i, d_j in itertools.pairwise([0, 1, 0, -1, 0]):
                    n_i, n_j = i + d_i, j + d_j
                    if (
                        not 0 <= n_i < m
                        or not 0 <= n_j < n
                        or (n_i, n_j) in blocked
                        or (n_i, n_j) in visited
                    ):
                        continue

                    if (n_i, n_j) == (m - 1, n - 1):
                        return steps

                    visited.add((n_i, n_j))
                    queue.append((n_i, n_j))

        return -1

    def part_2(
        self,
        filepath: Path,
        board_size: tuple[int, int] = (71, 71),
    ) -> str:
        def get_parent(
            parents: list[list[tuple[int, int]]], node: tuple[int, int]
        ) -> tuple[int, int]:
            """
            Get the parent.

            Args:
                parents: The parents matrix.
                node: The row and column index to get the parent of.

            Returns:
                The parent for the selected cell.
            """
            i, j = node
            return parents[i][j]

        def get_rank(ranks: list[list[int]], node: tuple[int, int]) -> int:
            """
            Get the rank.

            Args:
                ranks: The ranks matrix.
                node: The row and column index to get the rank of.

            Returns:
                The rank for the selected cell.
            """
            i, j = node
            return ranks[i][j]

        def find(
            parents: list[list[tuple[int, int]]], i: int, j: int
        ) -> tuple[int, int]:
            """
            Find the parent index.

            Args:
                parents: The parents matrix.
                i: The child row index.
                j: The child column index.

            Returns:
                The parent row and column index respectively.
            """
            while parents[i][j] != (i, j):
                parents[i][j] = i, j = get_parent(parents, parents[i][j])

            return i, j

        def union(
            parents: list[list[tuple[int, int]]],
            ranks: list[list[int]],
            x: tuple[int, int],
            y: tuple[int, int],
        ):
            """
            Union two points.

            Args:
                parents: The parents matrix.
                ranks: The ranks matrix.
                x: The row and column index of one point.
                y: The row and column index of another point.
            """
            x = find(parents, *x)
            y = find(parents, *y)

            if x == y:
                return

            if get_rank(ranks, x) < get_rank(ranks, y):
                (x, y) = (y, x)

            ranks[x[0]][x[1]] += get_rank(ranks, y)
            parents[y[0]][y[1]] = x

        m, n = board_size
        parents = [[(i, j) for j in range(n + 2)] for i in range(m + 2)]
        ranks = [[1] * (n + 2) for _ in range(m + 2)]
        visited = {(0, 1), (0, n + 1), (1, 0), (m + 1, 0)}

        # Join top and right
        for j in range(1, n + 1):
            union(parents, ranks, (0, j), (0, j + 1))
            visited.add((0, j + 1))
        for i in range(m):
            union(parents, ranks, (i, n + 1), (i + 1, n + 1))
            visited.add((i + 1, n + 1))

        # Join left and bottom
        for i in range(1, m + 1):
            union(parents, ranks, (i, 0), (i + 1, 0))
            visited.add((i + 1, 0))
        for j in range(n):
            union(parents, ranks, (m + 1, j), (m + 1, j + 1))
            visited.add((m + 1, j + 1))

        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                line = line.strip()
                j, i = line.split(",")
                i = int(i) + 1
                j = int(j) + 1

                visited.add((i, j))
                for d_i, d_j in itertools.product([-1, 0, 1], repeat=2):
                    if d_i == d_j == 0:
                        continue

                    if (i + d_i, j + d_j) in visited:
                        union(parents, ranks, (i, j), (i + d_i, j + d_j))

                if find(parents, 0, 1) == find(parents, 1, 0):
                    return line

        return ""
