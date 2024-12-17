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
    cases: list[tuple[str, int | str | None, int | str | None]]

    # === Test cases ===
    def pytest_generate_tests(self, metafunc: pytest.Metafunc):
        """
        Pytest runs this before tests are run. Tests cases are
        generated using the case attributes.

        Args:
            metafunc: The test function.
        """
        test_cases = [
            (i, (input_file, solution, part))
            for i, (input_file, *solutions) in enumerate(self.cases)
            for part, solution in enumerate(solutions, start=1)
            if solution is not None
        ]

        metafunc.parametrize(
            ["input_file", "solution", "part"],
            [param for _, param in test_cases],
            indirect=["input_file"],
            ids=[
                f"Test {test_id} - part {part}"
                for test_id, (*_, part) in test_cases
            ],
        )

    # === Fixtures ===
    @pytest.fixture
    def input_file(
        self,
        tmp_path: pathlib.Path,
        request: pytest.FixtureRequest,
    ) -> pathlib.Path:
        """
        Creates a temporary input file with the test input.

        Args:
            tmp_path: The temporary path to store the input file.

        Returns:
            Path to the temporary input file.
        """
        input_data = request.param
        input_file = tmp_path / "input.txt"
        with open(input_file, "w", encoding=sys.getdefaultencoding()) as file:
            file.write(input_data)
        return input_file

    # === Tests ===
    def test_part(self, input_file: pathlib.Path, solution: int, part: int):
        """
        Tests a part of the solver.
        """
        test_args = getattr(self, "test_args", {})
        assert (
            getattr(self.solver, f"part_{part}")(input_file, **test_args)
            == solution
        )
