"""
Base solver class
"""

from abc import ABC, abstractmethod
import inspect
from pathlib import Path


class Solver(ABC):
    """Base solver."""

    @abstractmethod
    def part_1(self, file: Path) -> int:
        """
        Solves part 1.

        Args:
            file: The path to the data file.

        Returns:
            The solution to part 1.
        """

    @abstractmethod
    def part_2(self, file: Path) -> int:
        """
        Solves part 2.

        Args:
            file: The path to the data file.

        Returns:
            The solution to part 2.
        """

    def solve(self, file: str | Path):
        """
        Run the solver.

        Args:
            file: The path to the data file.
        """
        file = Path(file)
        day_num = (
            solver_module.__package__[-2:].lstrip("0")
            if (solver_module := inspect.getmodule(self))
            and solver_module.__package__
            else "??"
        )
        print(f"Day {day_num}")
        print("Part 1:", self.part_1(file))
        print("===========================")
        print("Part 2:", self.part_2(file))

    def __init__(self, file: str | Path | None = None):
        """
        Base solver.

        Args:
            file: The path to the data file. If not provided, do nothing.
                If a file is provided, immediately solve.
        """
        if not file:
            return

        self.solve(file)
