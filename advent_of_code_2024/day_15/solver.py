"""
Day 15 solver.
"""

import collections
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 15 solver.
    """

    def _solve(self, filepath: Path, expand: bool = False) -> int:
        """
        Solves a part.

        Args:
            filepath: The path to the input file.
            expand: If true, expand the board, else keep the board
                as in the input.

        Returns:
            The solution to the part.
        """
        board = []
        robot = 0, 0
        expansion_map = {".": "..", "@": "@.", "O": "[]", "#": "##"}

        def move(robot, c) -> tuple[int, int]:
            i, j = robot
            d_i, d_j = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}[
                c
            ]

            to_move = [(i, j)]
            queue = collections.deque([(i + d_i, j + d_j)])
            visited = set(queue)
            while queue:
                i, j = queue.popleft()
                if board[i][j] == "#":
                    return robot

                if board[i][j] == ".":
                    continue

                to_move.append((i, j))

                if board[i][j] == "[":
                    if (i, j + 1) not in visited:
                        queue.append((i, j + 1))
                        visited.add((i, j + 1))

                if board[i][j] == "]":
                    if (i, j - 1) not in visited:
                        queue.append((i, j - 1))
                        visited.add((i, j - 1))

                if (i + d_i, j + d_j) in visited:
                    continue

                queue.append((i + d_i, j + d_j))
                visited.add((i + d_i, j + d_j))

            for i, j in reversed(to_move):
                board[i + d_i][j + d_j] = board[i][j]
                board[i][j] = "."

            i, j = robot
            return (i + d_i, j + d_j)

        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for i, line in enumerate(file):
                line = line.strip()
                if line == "":
                    break

                row = []
                for j, c in enumerate(line):
                    if c == "@":
                        robot = (i, j * (2 if expand else 1))

                    if expand:
                        c = expansion_map[c]

                    row.extend(c)
                board.append(row)

            for line in file:
                for c in line.strip():
                    robot = move(robot, c)

        result = 0
        search_char = "[" if expand else "O"
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != search_char:
                    continue
                result += 100 * i + j

        return result

    def part_1(self, filepath: Path) -> int:
        return self._solve(filepath)

    def part_2(self, filepath: Path) -> int:
        return self._solve(filepath, True)
