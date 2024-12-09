"""
Day 9 solver.
"""

import heapq
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 9 solver.
    """

    def part_1(self, filepath: Path) -> int:
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            line = file.read().strip()

        ids = []
        current = 0
        for i, c in enumerate(line):
            x = int(c)
            if i % 2 == 0:
                ids.extend([current] * x)
                current += 1
            else:
                ids.extend([-1] * x)

        left, right = 0, len(ids) - 1
        result = 0
        while left <= right:
            while left <= right and ids[left] != -1:
                result += left * ids[left]
                left += 1

            while left < right and ids[left] == -1 and ids[right] != -1:
                ids[left] = ids[right]
                ids[right] = -1
                result += left * ids[left]
                left += 1
                right -= 1

            while left < right and ids[right] == -1:
                right -= 1

        return result

    def part_2(self, filepath: Path) -> int:
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            line = file.read().strip()

        files = []
        free_spaces_per_length = [[] for _ in range(10)]
        current = 0
        for i, c in enumerate(line):
            x = int(c)
            if i % 2 == 0:
                files.append([current, x])
            else:
                free_spaces_per_length[x].append(current)

            current += x

        for i in reversed(range(len(files))):
            file = file_start, file_len = files[i]

            selected_len = -1
            for length in range(file_len, 10):
                if not free_spaces_per_length[length]:
                    continue

                if (
                    selected_len == -1
                    or free_spaces_per_length[length][0]
                    < free_spaces_per_length[selected_len][0]
                ):
                    selected_len = length

            if (
                selected_len == -1
                or file_start < free_spaces_per_length[selected_len][0]
            ):
                continue

            new_start = heapq.heappop(free_spaces_per_length[selected_len])
            file[0] = new_start
            if selected_len > file_len:
                heapq.heappush(
                    free_spaces_per_length[selected_len - file_len],
                    new_start + file_len,
                )

        return sum(
            i * x
            for x, (start, l) in enumerate(files)
            for i in range(start, start + l)
        )
