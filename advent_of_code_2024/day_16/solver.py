"""
Day 16 solver.
"""

import collections
import heapq
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 16 solver.
    """

    def _process(
        self, filepath: Path
    ) -> tuple[list[str], tuple[int, int], tuple[int, int]]:
        """
        Processes the input file.

        Args:
            filepath: The path to the input file.

        Returns:
            The board, start position and end position respectively.
        """
        board = []
        start = 0, 0
        end = 0, 0
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for i, line in enumerate(file):
                line = line.strip()
                board.append(line)
                for j, c in enumerate(line):
                    if c == "S":
                        start = i, j
                    elif c == "E":
                        end = i, j

        return board, start, end

    def part_1(self, filepath: Path) -> int:
        board, start, end = self._process(filepath)

        visited = {(*start, 0, 1): 0}
        heap = [(0, *start, 0, 1)]
        while heap:
            cost, i, j, d_i, d_j = heapq.heappop(heap)
            if (i, j) == end:
                return cost

            if (
                (next_state := (i + d_i, j + d_j, d_i, d_j)) not in visited
                or cost + 1 < visited[next_state]
            ) and board[i + d_i][j + d_j] != "#":
                new_cost = cost + 1
                visited[next_state] = new_cost
                heapq.heappush(heap, (new_cost, *next_state))

            if (
                next_state := (i, j, -d_j, d_i)
            ) not in visited or cost + 1000 < visited[next_state]:
                new_cost = cost + 1000
                visited[next_state] = new_cost
                heapq.heappush(heap, (new_cost, *next_state))

            if (
                next_state := (i, j, d_j, -d_i)
            ) not in visited or cost + 1000 < visited[next_state]:
                new_cost = cost + 1000
                visited[next_state] = new_cost
                heapq.heappush(heap, (new_cost, *next_state))

        return -1

    def part_2(self, filepath: Path) -> int:
        board, start, end = self._process(filepath)

        visited = {(*start, 0, 1): 0}
        heap = [(0, *start, 0, 1)]
        parents = collections.defaultdict(set)
        target = float("inf")
        ends = set()
        while heap:
            cost, i, j, d_i, d_j = heapq.heappop(heap)
            if cost > target:
                break

            origin = i, j, d_i, d_j
            if cost > visited[origin]:
                continue

            if (i, j) == end:
                target = cost
                ends.add(origin)
                continue

            candidates = [
                (i, j, -d_j, d_i, cost + 1000),  # Rotate left
                (i, j, d_j, -d_i, cost + 1000),  # Rotate right
                (i + d_i, j + d_j, d_i, d_j, cost + 1),  # Move forward
            ]
            if board[i + d_i][j + d_j] == "#":
                candidates.pop()

            for i, j, d_i, d_j, new_cost in candidates:
                next_state = i, j, d_i, d_j
                if next_state in visited and new_cost > visited[next_state]:
                    continue

                if origin in parents[next_state]:
                    continue

                if next_state in visited and new_cost < visited[next_state]:
                    parents[next_state].clear()

                parents[next_state].add(origin)
                visited[next_state] = new_cost
                heapq.heappush(heap, (new_cost, *next_state))

        visited = set(ends)
        stack = list(ends)
        while stack:
            node = stack.pop()
            for parent in parents[node]:
                if parent in visited:
                    continue

                visited.add(parent)
                stack.append(parent)

        return len({node[:2] for node in visited})
