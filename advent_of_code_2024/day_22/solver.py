"""
Day 22 solver.
"""

import itertools
from multiprocessing import Pool
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 22 solver.
    """

    def _part_1(self, line) -> int:
        MOD = 16777216
        num = int(line.strip())
        for _ in range(2000):
            num ^= num * 64
            num %= MOD
            num ^= num // 32
            num %= MOD
            num ^= num * 2048
            num %= MOD

        return num

    def part_1(self, filepath: Path) -> int:
        with (
            open(filepath, "r", encoding=sys.getdefaultencoding()) as file,
            Pool() as pool,
        ):
            return sum(pool.imap_unordered(self._part_1, file))

    def _part_2(
        self,
        line: str,
    ) -> list[tuple[int, int, int, int, int]]:
        MOD = 16777216
        num = int(line.strip())
        result = []
        seen = [
            [[[False] * 20 for _ in range(20)] for _ in range(20)]
            for _ in range(10)
        ]
        c_0 = c_1 = c_2 = c_3 = 0
        for i in range(2000):
            prev_num = num
            num ^= num * 64
            num %= MOD
            num ^= num // 32
            num %= MOD
            num ^= num * 2048
            num %= MOD

            c_0, c_1, c_2, c_3 = c_1, c_2, c_3, num % 10 - prev_num % 10

            if i >= 3 and c_3 > 0:
                if seen[c_0][c_1][c_2][c_3]:
                    continue

                seen[c_0][c_1][c_2][c_3] = True
                result.append((c_0, c_1, c_2, c_3, num % 10))

        return result

    def part_2(self, filepath: Path) -> int:
        result = [
            [[[0] * 10 for _ in range(20)] for _ in range(20)]
            for _ in range(20)
        ]
        with (
            open(filepath, "r", encoding=sys.getdefaultencoding()) as file,
            Pool() as pool,
        ):
            for line_result in pool.imap_unordered(self._part_2, file):
                for i, j, k, l, x in line_result:
                    result[i][j][k][l] += x

        return max(
            result[i][j][k][l]
            for i, j, k in itertools.product(range(20), repeat=3)
            for l in range(10)
        )
