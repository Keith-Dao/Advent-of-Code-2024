"""
Day 14 solver.
"""

from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 14 solver.
    """

    def part_1(
        self, filepath: Path, size: tuple[int, int] = (103, 101)
    ) -> int:
        m, n = size
        locations = []
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                p, v = line.strip().split()
                p_j, p_i = (int(x) for x in p[2:].split(","))
                v_j, v_i = (int(x) for x in v[2:].split(","))
                i = (p_i + v_i * 100) % m
                j = (p_j + v_j * 100) % n
                locations.append((i, j))

        quadrant = [0] * 4
        for i, j in locations:
            if i == m // 2 or j == n // 2:
                continue
            q_i, q_j = i // ((m + 1) // 2), j // ((n + 1) // 2)
            quadrant[q_i * 2 + q_j] += 1

        result = 1
        for x in quadrant:
            result *= x
        return result

    def part_2(
        self, filepath: Path, size: tuple[int, int] = (103, 101)
    ) -> int:
        m, n = size
        robots = []
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                p, v = line.strip().split()
                p_j, p_i = (int(x) for x in p[2:].split(","))
                v_j, v_i = (int(x) for x in v[2:].split(","))
                robots.append((p_i, p_j, v_i, v_j))

        result = 0
        while True:
            result += 1
            seen = set()
            for k, (i, j, d_i, d_j) in enumerate(robots):
                robots[k] = ((i + d_i) % m, (j + d_j) % n, d_i, d_j)
                seen.add((robots[k][:2]))

            if len(seen) == len(robots):
                break

        return result
