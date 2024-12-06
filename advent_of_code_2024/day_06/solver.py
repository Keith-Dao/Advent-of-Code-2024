"""
Day 6 solver.
"""

import bisect
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 6 solver.
    """

    def _parse_file(
        self, filepath: Path
    ) -> tuple[set[tuple[int, int]], tuple[int, int], int, int]:
        """
        Parse the file and extract the obstacles, starting position
        and the number of rows and columns.

        Args:
            filepath: Path to the input file.

        Returns:
            The obstacle locations, starting position, number of rows
            and number of columns respectively.
        """
        obstacles = set()
        pos = 0, 0
        m = n = 0
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for i, line in enumerate(file):
                line = line.strip()
                for j, x in enumerate(line):
                    if x == "#":
                        obstacles.add((i, j))
                    elif x == "^":
                        pos = i, j

                m += 1
                n = len(line)

        return obstacles, pos, m, n

    def part_1(self, filepath: Path) -> int:
        obstacles, (i, j), m, n = self._parse_file(filepath)
        visited = set()
        d_i, d_j = -1, 0
        while 0 <= i < m and 0 <= j < n:
            visited.add((i, j))
            while (i + d_i, j + d_j) in obstacles:
                d_i, d_j = d_j, -d_i
            i += d_i
            j += d_j

        return len(visited)

    def part_2(self, filepath: Path) -> int:
        def next_position(
            obstacle_list: list[int],
            x: int,
            d_x: int,
            upper_limit: int,
        ) -> int:
            """
            Find the next valid position.

            Args:
                obstacle_list: Sorted list of the obstacle locations in the axis of traversal.
                x: The current position.
                d_x: The direction of travel.
                upper_limit: The upper bound of the grid space.

            Returns:
                The next location to travel to before being stopped.
            """
            i = bisect.bisect_left(obstacle_list, x) - (d_x == -1)
            if not 0 <= i < len(obstacle_list):
                return upper_limit

            return obstacle_list[i] - d_x

        def does_loop_with_extra_obstacle(
            prev_visited: set[tuple[int, int, int, int]],
            obstacles: set[tuple[int, int]],
            tried_obstacles: set[tuple[int, int]],
            row_list: list[list[int]],
            col_list: list[list[int]],
            i: int,
            j: int,
            d_i: int,
            d_j: int,
            m: int,
            n: int,
        ) -> bool:
            """
            Checks if the path loops if an immediate obstacle is added.

            Args:
                prev_visited: The previously visited location and direction.
                obstacles: The original obstacle positions.
                tried_obstacles: The new obstacle positions that have been tried.
                row_list: Sorted adjacency list for obstacles in a row.
                col_list: Sorted adjacency list for obstacles in a column.
                i: The row index.
                j: The column index.
                d_i: The row index direction.
                d_j: The column index direction.
                m: The number of rows.
                n: The number of columns.

            Returns:
                True if the path loops with the new obstacle, else false.
            """
            while (i + d_i, j + d_j) in obstacles:
                d_i, d_j = d_j, -d_i

            if (
                not 0 <= i + d_i < m
                or not 0 <= j + d_j < n
                or (i + d_i, j + d_j) in tried_obstacles
            ):
                return False

            o_i, o_j = new_obstacle = i + d_i, j + d_j
            bisect.insort(row_list[o_i], o_j)
            bisect.insort(col_list[o_j], o_i)
            obstacles.add(new_obstacle)

            visited = set()
            while (
                0 <= i < m
                and 0 <= j < n
                and (i, j, d_i, d_j) not in prev_visited
                and (i, j, d_i, d_j) not in visited
            ):
                visited.add((i, j, d_i, d_j))
                while (i + d_i, j + d_j) in obstacles:
                    d_i, d_j = d_j, -d_i

                if d_i == 0:
                    j = next_position(row_list[i], j, d_j, n)
                else:
                    i = next_position(col_list[j], i, d_i, m)

            row_list[o_i].remove(o_j)
            col_list[o_j].remove(o_i)
            obstacles.remove(new_obstacle)
            tried_obstacles.add(new_obstacle)

            return 0 <= i < m and 0 <= j < n

        obstacles, (i, j), m, n = self._parse_file(filepath)
        tried_obstacles = set()

        row_list = [[] for _ in range(m)]
        col_list = [[] for _ in range(n)]
        for x, y in obstacles:
            row_list[x].append(y)
            col_list[y].append(x)
        for row in row_list:
            row.sort()
        for col in col_list:
            col.sort()

        visited = set()
        d_i, d_j = -1, 0
        result = 0
        while 0 <= i < m and 0 <= j < n:
            result += does_loop_with_extra_obstacle(
                visited,
                obstacles,
                tried_obstacles,
                row_list,
                col_list,
                i,
                j,
                d_i,
                d_j,
                m,
                n,
            )

            visited.add((i, j, d_i, d_j))
            while (i + d_i, j + d_j) in obstacles:
                d_i, d_j = d_j, -d_i

            i += d_i
            j += d_j

        return result
