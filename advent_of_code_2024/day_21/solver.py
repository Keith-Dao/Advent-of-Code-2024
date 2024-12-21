"""
Day 21 solver.
"""

from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 21 solver.
    """

    def _solve(self, filepath: Path, depth: int) -> int:
        """
        Solves a part.

        Args:
            filepath: The path to the input file.
            depth: The depth level.

        Returns:
            The solution to the part.
        """

        def solve(
            sequence: str,
            mapping: dict[str, tuple[int, int]],
            next_mapping: dict[str, tuple[int, int]],
            count: int,
            memo: dict[tuple[str, int], int],
        ) -> int:
            if count == 0:
                return len(sequence)

            if (sequence, count) in memo:
                return memo[(sequence, count)]

            result = 0
            current = mapping["A"]
            for c in sequence:
                target = mapping[c]
                i, j = current
                n_i, n_j = target

                d_i = n_i - i
                d_j = n_j - j
                vertical_direction = "^" if d_i < 0 else "v"
                horizontal_direction = "<" if d_j < 0 else ">"

                candidate_moves = []

                if mapping[" "] != (i, n_j):
                    move = []
                    move.extend(horizontal_direction * abs(d_j))
                    move.extend(vertical_direction * abs(d_i))
                    move.append("A")
                    candidate_moves.append(move)

                if mapping[" "] != (n_i, j):
                    move = []
                    move.extend(vertical_direction * abs(d_i))
                    move.extend(horizontal_direction * abs(d_j))
                    move.append("A")
                    candidate_moves.append(move)

                result += min(
                    solve(
                        "".join(move),
                        next_mapping,
                        next_mapping,
                        count - 1,
                        memo,
                    )
                    for move in candidate_moves
                )
                current = target

            memo[(sequence, count)] = result
            return result

        num_map = {
            c: (i, j)
            for i, row in enumerate(["789", "456", "123", " 0A"])
            for j, c in enumerate(row)
        }
        dir_map = {
            c: (i, j)
            for i, row in enumerate([" ^A", "<v>"])
            for j, c in enumerate(row)
        }
        memo = {}

        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            return sum(
                int((line := unstripped_line.strip())[:-1])
                * solve(line, num_map, dir_map, depth, memo)
                for unstripped_line in file
            )

    def part_1(self, filepath: Path) -> int:
        return self._solve(filepath, 3)

    def part_2(self, filepath: Path) -> int:
        return self._solve(filepath, 26)
