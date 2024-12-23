"""
Day 23 solver.
"""

import collections
import itertools
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 23 solver.
    """

    def part_1(self, filepath: Path) -> int:
        graph = collections.defaultdict(set)

        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                u, v = line.strip().split("-")
                graph[u].add(v)
                graph[v].add(u)

        seen = set()
        for node, next_ in graph.items():
            if node[0] != "t":
                continue

            for node_1, node_2 in itertools.combinations(next_, 2):
                if node_1 in graph[node_2]:
                    seen.add(tuple(sorted([node, node_1, node_2])))

        return len(seen)

    def part_2(self, filepath: Path) -> str:
        graph = collections.defaultdict(set)

        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                u, v = line.strip().split("-")
                graph[u].add(v)
                graph[v].add(u)

        result = []
        stack = [(set(), set(graph.keys()), set())]
        while stack:
            candidates, vertices, excluded = stack.pop()
            if not vertices and not excluded:
                result = max(result, candidates, key=len)

            if not vertices:
                continue

            pivot = next(iter(vertices | excluded))
            for v in vertices - graph[pivot]:
                stack.append(
                    (
                        candidates | {v},
                        vertices & graph[v],
                        excluded & graph[v],
                    )
                )
                vertices.remove(v)
                excluded.add(v)

        return ",".join(sorted(result))
