"""
Day 13 solver.
"""

from pathlib import Path
import re
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 13 solver.
    """

    def _solve_line(
        self,
        a_xy: tuple[int, int],
        b_xy: tuple[int, int],
        prize_xy: tuple[int, int],
    ) -> int:
        """
        Solves one line.

        Args:
            a_xy: The X and Y values for the A button.
            b_xy: The X and Y values for the B button.
            prize_xy: The X and Y positions for the prize.

        Returns:
            The solution to the part, or zero if it cannot be solved.
        """
        a_x, a_y = a_xy
        b_x, b_y = b_xy
        prize_x, prize_y = prize_xy

        a = (prize_x * b_y - prize_y * b_x) / (a_x * b_y - a_y * b_x)
        if a != int(a):
            return 0

        b = (prize_x - a * a_x) / b_x
        if b != int(b):
            return 0

        return int(a) * 3 + int(b)

    def _solve(self, filepath: Path, prize_offset: int = 0) -> int:
        """
        Solves a part.

        Args:
            filepath: The path to the input file.

        Returns:
            Solution to the part.
        """

        def extract_nums(line: str, offset: int = 0) -> tuple[int, int]:
            """
            Extracts the numbers from the line.

            Args:
                line: The line to extract the numbers from.
                offset: Offset to add to the extracted number.

            Returns:
                The X and Y values.
            """
            xy = re.match(r"[^\d]+(\d+)[^\d]+(\d+)", line)
            assert xy is not None
            return int(xy.group(1)) + offset, int(xy.group(2)) + offset

        result = 0
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            line = file.readline()
            while line.strip():
                result += self._solve_line(
                    extract_nums(line),
                    extract_nums(file.readline()),
                    extract_nums(file.readline(), prize_offset),
                )

                file.readline()  # Blank line
                line = file.readline()
        return result

    def part_1(self, filepath: Path) -> int:
        return self._solve(filepath)

    def part_2(self, filepath: Path) -> int:
        return self._solve(filepath, 10000000000000)
