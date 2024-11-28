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
    part_1_solution: int
    part_2_solution: int

    # === Fixtures ===
    @pytest.fixture
    def input_file(self, tmp_path: pathlib.Path) -> pathlib.Path:
        """
        Create a temporary file with the example input.

        Args:
            tmp_path: The temporary path to store the input file.

        Returns:
            Path to the temporary input file.
        """
        input_file = tmp_path / "input.txt"
        with open(input_file, "w", encoding=sys.getdefaultencoding()) as file:
            file.write(self.example_input)
        return input_file

    # === Tests ===
    def test_part_1(self, input_file):
        """
        Test part 1 solver.
        """
        assert self.solver.part_1(input_file) == self.part_1_solution

    def test_part_2(self, input_file):
        """
        Test part 2 solver.
        """
        assert self.solver.part_2(input_file) == self.part_2_solution
