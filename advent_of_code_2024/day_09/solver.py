"""
Day 9 solver.
"""

import heapq
from pathlib import Path
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 9 solver.
    """

    def part_1(self, filepath: Path) -> int:
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            line = file.read().strip()

        ids = []
        current = 0
        for i, c in enumerate(line):
            x = int(c)
            if i % 2 == 0:
                ids.extend([current] * x)
                current += 1
            else:
                ids.extend([-1] * x)

        left, right = 0, len(ids) - 1
        result = 0
        while left <= right:
            while left <= right and ids[left] != -1:
                result += left * ids[left]
                left += 1

            while left < right and ids[left] == -1 and ids[right] != -1:
                ids[left] = ids[right]
                ids[right] = -1
                result += left * ids[left]
                left += 1
                right -= 1

            while left < right and ids[right] == -1:
                right -= 1

        return result

    def part_2(self, filepath: Path) -> int:
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            line = file.read().strip()

        files = []
        free_spaces_with_length = [[] for _ in range(10)]
        current = 0
        for i, c in enumerate(line):
            x = int(c)
            if i % 2 == 0:
                files.append([current, x])
            else:
                free_spaces_with_length[x].append(current)

            current += x

        for i in reversed(range(len(files))):
            file = file_start, file_len = files[i]

            selected_len = -1
            for length in range(file_len, 10):
                if not free_spaces_with_length[length]:
                    continue

                if (
                    selected_len == -1
                    or free_spaces_with_length[length][0]
                    < free_spaces_with_length[selected_len][0]
                ):
                    selected_len = length

            if (
                selected_len == -1
                or file_start < free_spaces_with_length[selected_len][0]
            ):
                continue

            new_start = heapq.heappop(free_spaces_with_length[selected_len])
            file[0] = new_start
            if selected_len > file_len:
                heapq.heappush(
                    free_spaces_with_length[selected_len - file_len],
                    new_start + file_len,
                )

        return sum(
            x * (start * length + length * (length - 1) // 2)
            for x, (start, length) in enumerate(files)
        )

    def _alternate_part_2(self, filepath: Path) -> int:
        """
        Solves part two using a segment tree. Slower than other part two solver.

        Args:
            filepath: Path to the input file.

        Returns:
            The solution to part two.
        """
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            line = file.read().strip()

        n = len(line)
        tree = [(-1, -1) for _ in range(4 * n)]

        def update(
            index: int,
            length: int,
            i: int = 0,
            left: int = 0,
            right: int = n - 1,
        ):
            """
            Update the segment tree with the new length at the block index.

            Args:
                index: The block's index.
                length: The new length of the block.
                i: The index of the tree.
                left: The left bound of the array.
                right: The right bound of the array.
            """
            if left == right:
                tree[i] = (length, index)
                return

            mid = (left + right) // 2
            if index <= mid:
                update(index, length, i * 2 + 1, left, mid)
            else:
                update(index, length, i * 2 + 2, mid + 1, right)

            tree[i] = max(tree[i * 2 + 1], tree[i * 2 + 2])

        def query(
            length: int, i: int = 0, left: int = 0, right: int = n - 1
        ) -> tuple[int, int]:
            """
            Query the segment tree for the lowest index with at least length
            available.

            Args:
                length: The minimum free block length.
                i: The index of the tree.
                left: The left bound of the array.
                right: The right bound of the array.

            Returns:
                The free block length and index respectively.
            """
            if left == right:
                if tree[i][0] >= length:
                    return tree[i]
                return (-1, -1)

            mid = (left + right) // 2
            if tree[i * 2 + 1][0] >= length:
                return query(length, i * 2 + 1, left, mid)

            if tree[i * 2 + 2][0] >= length:
                return query(length, i * 2 + 2, mid + 1, right)

            return (-1, -1)

        blocks = []
        current = 0
        for i, c in enumerate(line):
            x = int(c)
            if i % 2 == 1:
                update(i, x)

            blocks.append([current, x])
            current += x

        for i in reversed(range(len(blocks))):
            if i % 2 == 1:
                continue

            file = _, file_len = blocks[i]
            j = query(file_len)[1]
            if j == -1 or j > i:
                continue

            file[0] = blocks[j][0]
            blocks[j][0] += file_len
            blocks[j][1] -= file_len
            update(j, blocks[j][1])

        return sum(
            x // 2 * (start * length + length * (length - 1) // 2)
            for x, (start, length) in enumerate(blocks)
            if x % 2 == 0
        )
