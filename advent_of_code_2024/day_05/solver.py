"""
Day 5 solver.
"""

import collections
from io import TextIOWrapper
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 5 solver.
    """

    def _generate_graph(self, file: TextIOWrapper) -> dict[str, set[str]]:
        """
        Generates the graph.

        Note: This mutates the file object.

        Args:
            file: The opened file to read from.

        Returns:
            Mapping from number to all the numbers it must come before.
        """
        graph = collections.defaultdict(set)
        for line in file:
            if line.strip() == "":
                break

            x, y = line.strip().split("|")
            graph[x].add(y)
        return graph

    def _is_ordered(self, graph: dict[str, set[str]], nums: list[str]) -> bool:
        """
        Checks that the numbers are correctly ordered.

        Args:
            graph: Mapping from a number to all the numbers it should come before.
            nums: The number sequence.

        Returns:
            True if the numbers are ordered, else false.
        """
        previous = set()
        for x in nums:
            if graph[x] & previous:
                return False

            previous.add(x)
        return True

    def part_1(self, filepath: Path) -> int:
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            graph = self._generate_graph(file)

            return sum(
                int(nums[len(nums) // 2])
                for line in file
                if self._is_ordered(graph, nums := line.strip().split(","))
            )

    def part_2(self, filepath: Path) -> int:
        result = 0
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            graph = self._generate_graph(file)
            for line in file:
                nums = line.strip().split(",")
                if self._is_ordered(graph, nums):
                    continue

                in_degrees = {x: 0 for x in nums}
                for node in nums:
                    for next_ in in_degrees.keys() & graph[node]:
                        in_degrees[next_] += 1

                order = []
                queue = collections.deque(
                    [x for x, c in in_degrees.items() if c == 0]
                )
                while queue:
                    node = queue.popleft()
                    order.append(node)

                    for next_ in in_degrees.keys() & graph[node]:
                        in_degrees[next_] -= 1
                        if in_degrees[next_] == 0:
                            queue.append(next_)

                result += int(order[len(order) // 2])

        return result
