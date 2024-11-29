"""
CLI tool to run solver.
"""

import argparse
import importlib
import pathlib


def solver_day(value: str) -> int:
    """
    Validates that the argument is a valid day and converts it to an int.

    Args:
        value: The value from the CLI.

    Returns:
        The day number.

    Raises:
        ArgumentTypeError: Value was not an integer.
        ArgumentTypeError: Value was not in [1, 25].
    """
    try:
        day = int(value)
    except Exception as exc:
        raise argparse.ArgumentTypeError("Must be an integer.") from exc

    if not 1 <= day <= 25:
        raise argparse.ArgumentTypeError(
            "Must be in the range of 1 to 25 inclusively."
        )
    return day


def get_args() -> argparse.Namespace:
    """
    Gets the CLI args.

    Returns:
        The arguments from the CLI.
    """
    parser = argparse.ArgumentParser(
        prog="aoc_2024_solver",
        description="Runs solver for advent of code 2024.",
    )
    parser.add_argument(
        "day",
        type=solver_day,
        choices=range(1, 26),
        metavar="day",
        help="Day to solve.",
    )
    parser.add_argument(
        "filepath",
        nargs="?",
        type=pathlib.Path,
        default="input.txt",
        help="Input data filepath.",
    )
    return parser.parse_args()


def main():
    """
    Runs the solver selected in the CLI.
    """
    args = get_args()
    module = importlib.import_module(
        f".day_{args.day:02}", "advent_of_code_2024"
    )
    getattr(module, "Solver")(args.filepath)


if __name__ == "__main__":
    main()
