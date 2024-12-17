"""
Day 17 solver.
"""

from pathlib import Path
import re
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 17 solver.
    """

    def _process(self, filepath: Path) -> tuple[dict[str, int], list[str]]:
        registers = {}
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                line = line.strip()
                if line == "":
                    break

                if match := re.match(r"Register (.): (\d+)", line):
                    registers[match.group(1)] = int(match.group(2))

            program = file.read().strip().split()[1].split(",")

        return registers, program

    def part_1(self, filepath: Path) -> str:
        registers, program = self._process(filepath)

        output = []
        i = 0
        while i < len(program):
            opcode = program[i]
            operand = int(program[i + 1])
            i += 2

            combo_operand = operand
            if operand == 4:
                combo_operand = registers["A"]
            elif operand == 5:
                combo_operand = registers["B"]
            elif operand == 6:
                combo_operand = registers["C"]

            if opcode == "0":
                registers["A"] = registers["A"] >> combo_operand
            elif opcode == "1":
                registers["B"] = registers["B"] ^ operand
            elif opcode == "2":
                registers["B"] = combo_operand % 8
            elif opcode == "3" and registers["A"] != 0:
                i = operand
            elif opcode == "4":
                registers["B"] = registers["B"] ^ registers["C"]
            elif opcode == "5":
                output.append(combo_operand % 8)
            elif opcode == "6":
                registers["B"] = registers["A"] >> combo_operand
            elif opcode == "7":
                registers["C"] = registers["A"] >> combo_operand

        return ",".join(str(x) for x in output)

    def part_2(self, filepath: Path) -> int:
        register, program = self._process(filepath)

        def get_result(
            a: int,
            program: list[str],
            original_register: dict[str, int],
        ) -> int:
            """
            Get the first output that occurs. If the program halts,
            before a value is outputted, -1 is returned.

            Args:
                a: The value of register A to simulate.
                program: The program instructions.
                original_register: The original register.

            Returns:
                The outputted value or -1 if no value is outputted.
            """
            registers = original_register | {"A": a}
            i = 0
            while i < len(program):
                opcode = program[i]
                operand = int(program[i + 1])
                i += 2

                combo_operand = operand
                if operand == 4:
                    combo_operand = registers["A"]
                elif operand == 5:
                    combo_operand = registers["B"]
                elif operand == 6:
                    combo_operand = registers["C"]

                if opcode == "0":
                    registers["A"] = registers["A"] >> combo_operand
                elif opcode == "1":
                    registers["B"] = registers["B"] ^ operand
                elif opcode == "2":
                    registers["B"] = combo_operand % 8
                elif opcode == "3" and registers["A"] != 0:
                    i = operand
                elif opcode == "4":
                    registers["B"] = registers["B"] ^ registers["C"]
                elif opcode == "5":
                    return combo_operand % 8
                elif opcode == "6":
                    registers["B"] = registers["A"] >> combo_operand
                elif opcode == "7":
                    registers["C"] = registers["A"] >> combo_operand

            return -1

        candidate_as = {0}
        for num in reversed(program):
            next_candidate_as = set()
            for x in candidate_as:
                for new_x in range(8):
                    candidate_a = (x << 3) + new_x
                    if get_result(candidate_a, program, register) == int(num):
                        next_candidate_as.add(candidate_a)

            candidate_as = next_candidate_as

        return min(candidate_as)
