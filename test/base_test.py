"""
Base test.
"""

import pathlib
import sys

import pytest

from advent_of_code_2024.base import Solver


class BaseTests:
    """Base tests"""

    solver: Solver
    example_input: str
    part_1_input: str
    part_2_input: str
    part_1_solution: int
    part_2_solution: int

    # === Fixtures ===
    @pytest.fixture
    def part(
        self,
        tmp_path: pathlib.Path,
        request: pytest.FixtureRequest,
    ) -> tuple[int, pathlib.Path, int]:
        """
        Creates a temporary input file the selected example input
        and gathers the part to test and the expected answer.

        Args:
            tmp_path: The temporary path to store the input file.

        Returns:
            The part to be tested, path to the temporary input file
            and the solution to the part.
        """
        part_num = request.param
        input_file = tmp_path / "input.txt"
        with open(input_file, "w", encoding=sys.getdefaultencoding()) as file:
            file.write(
                getattr(self, f"part_{part_num}_input")
                if hasattr(self, f"part_{part_num}_input")
                # Fallback to the general example input
                else self.example_input
            )
        return part_num, input_file, getattr(self, f"part_{part_num}_solution")

    # === Tests ===
    @pytest.mark.parametrize("part", [1, 2], indirect=True)
    def test_part(self, part):
        """
        Tests a part of the solver.
        """
        part_num, input_file, solution = part
        assert getattr(self.solver, f"part_{part_num}")(input_file) == solution
