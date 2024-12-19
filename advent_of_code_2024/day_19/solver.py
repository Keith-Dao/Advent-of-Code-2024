"""
Day 19 solver.
"""

from pathlib import Path
import sys
from typing import Any, Callable, Optional

from ..base import Solver as BaseSolver


class Trie:
    """
    Trie node.
    """

    children: list[Optional["Trie"]]
    word: str | None = None

    def __init__(self):
        self.children = [None] * 26

    @staticmethod
    def parse_key(
        func: Callable[["Trie", int], Any]
    ) -> Callable[["Trie", str], Any]:
        """
        Checks the key and parses it into an index,

        Args:
            func: The function to wrap around.

        Returns:
            The wrapped function.
        """

        def check(self, key: str) -> Any:
            if not "a" <= key <= "z":
                raise ValueError("Invalid key")

            return func(self, ord(key) - ord("a"))

        return check

    @parse_key
    def __getitem__(self, i: int) -> "Trie":
        result = self.children[i]
        if not result:
            result = self.children[i] = Trie()
        return result

    @parse_key
    def __contains__(self, i: int) -> bool:
        return self.children[i] is not None


class Solver(BaseSolver):
    """
    Day 19 solver.
    """

    def part_1(self, filepath: Path) -> int:
        trie = Trie()
        memo = {}

        def is_valid(line: str, trie: Trie, memo: dict[str, bool]) -> bool:
            """
            Check if the line can be constructed.

            Args:
                line: The line to construct.
                trie: The root trie node.
                memo: The memoised solutions.

            Returns:
                True if the line can be constructed, else false.
            """
            if line == "":
                return True

            if line in memo:
                return memo[line]

            curr = trie
            for i, c in enumerate(line):
                if c not in curr:
                    break

                curr = curr[c]
                if curr.word is not None and is_valid(
                    line[i + 1 :], trie, memo
                ):
                    memo[line] = True
                    return True

            memo[line] = False
            return False

        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            line = file.readline().strip()
            for word in line.split(", "):
                curr = trie
                for c in word:
                    curr = curr[c]
                curr.word = word

            file.readline()  # Blank line

            return sum(is_valid(line.strip(), trie, memo) for line in file)

    def part_2(self, filepath: Path) -> int:
        trie = Trie()
        memo = {}

        def count(line: str, trie: Trie, memo: dict[str, int]) -> int:
            """
            Count the number of unique permutations.

            Args:
                line: The line to construct.
                trie: The root trie node.
                memo: The memoised results.

            Returns:
                The number of unique permutations.
            """
            if line == "":
                return 1

            if line in memo:
                return memo[line]

            result = 0
            curr = trie
            for i, c in enumerate(line):
                if c not in curr:
                    break

                curr = curr[c]
                if curr.word is not None:
                    result += count(line[i + 1 :], trie, memo)

            memo[line] = result
            return result

        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            line = file.readline().strip()
            for word in line.split(", "):
                curr = trie
                for c in word:
                    curr = curr[c]
                curr.word = word

            file.readline()  # Blank line

            return sum(count(line.strip(), trie, memo) for line in file)
