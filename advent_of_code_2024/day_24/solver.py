"""
Day 24 solver.
"""

import collections
from pathlib import Path
import re
import sys

from ..base import Solver as BaseSolver


class Solver(BaseSolver):
    """
    Day 24 solver.
    """

    def part_1(self, filepath: Path) -> int:
        node_values = {}
        gates = {}
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                line = line.strip()
                if line == "":
                    break

                if match := re.match(r"(.+): (\d)", line):
                    node_values[match.group(1)] = match.group(2) == "1"

            for line in file:
                line = line.strip()
                inputs, output = line.split(" -> ")
                x, op, y = inputs.split()

                gates[output] = (x, op, y)

        nodes = set(node_values.keys()) | set(gates.keys())

        def compute(node_values: dict[str, int], node: str) -> int:
            """
            Compute the value at a node.

            Args:
                node_values: Stored node values.
                node: The node to compute the value for.

            Returns:
                The value of the node.

            Raises;
                ValueError: An invalid operation was provided.
            """
            if node in node_values:
                return node_values[node]

            def compute_value(node: str) -> int:
                """
                Computes the node value.

                Args:
                    node: The node to compute the value for.

                Returns:
                    The value of the node.

                Raises;
                    ValueError: An invalid operation was provided.
                """
                x, op, y = gates[node]
                if op == "AND":
                    return compute(node_values, x) and compute(node_values, y)

                if op == "OR":
                    return compute(node_values, x) or compute(node_values, y)

                if op == "XOR":
                    return compute(node_values, x) ^ compute(node_values, y)

                raise ValueError(f"{op} is not a valid operation.")

            node_values[node] = compute_value(node)
            return node_values[node]

        result = 0
        for node in nodes:
            if node[0] != "z":
                continue

            shift = int(node[1:])
            result |= compute(node_values, node) << shift
        return result

    def part_2(self, filepath: Path) -> str:
        bit_count = 0
        gates = {}
        edges = collections.defaultdict(set)
        with open(filepath, "r", encoding=sys.getdefaultencoding()) as file:
            for line in file:
                line = line.strip()
                if line == "":
                    break

                bit_count += 1

            for line in file:
                line = line.strip()
                inputs, output = line.split(" -> ")
                x, op, y = inputs.split()

                gates[output] = (x, op, y)
                edges[x].add(output)
                edges[y].add(output)

        bit_count //= 2

        # ======================================================================================
        # Full adder architecture
        #
        # Inputs:
        # x: Input x
        # y: Input y
        # cin: Carry in
        #
        # Internals:
        # in_xor: x XOR y
        # and_0: x AND y
        # and_1: in_xor AND cin
        #
        # Outputs:
        # z: in_xor XOR cin
        # cout: and_0 OR and_1
        #
        # Solution from:
        # https://github.com/piman51277/AdventOfCode/blob/master/solutions/2024/24/index2prog.js
        # ======================================================================================

        def check_xor_gates(
            gates: dict[str, tuple[str, str, str]], result: set[str]
        ):
            """
            Checks that the gates with XOR operations are:
                - input XOR gates that does not output to z
                    - except for the first z gate that should be
                    a input XOR gate
                - outputting to z if not an input XOR gate

            Args:
                gates: Mapping from output gates to the input nodes and operation.
                result: The set of nodes that are invalid.
            """
            for gate, (x, op, _) in gates.items():
                if op != "XOR":
                    continue

                if x[0] in "xy":  # xor gate
                    if (int(x[1:]) == 0) ^ (gate[0] == "z"):
                        result.add(gate)
                elif gate[0] != "z":  # z gate
                    result.add(gate)

        def check_z_gates(
            gates: dict[str, tuple[str, str, str]],
            result: set[str],
            bit_count: int,
        ):
            """
            Checks that the z gates have:
                - an input XOR operation if it is not the last z gate
                - an input OR operation if it is the last z gate

            Args:
                gates: Mapping from output gates to the input nodes and operation.
                result: The set of nodes that are invalid.
                bit_count: The bit count of the largest z state.
            """
            for gate, (_, op, _) in gates.items():
                if gate[0] != "z":
                    continue

                if (
                    int(gate[1:]) == bit_count
                ):  # Last output bit is the carry bit
                    if op != "OR":
                        result.add(gate)
                    continue

                if op != "XOR":
                    result.add(gate)

        def check_in_xor_outputs_to_z_gates(
            gates: dict[str, tuple[str, str, str]], result: set[str]
        ):
            """
            Checks that the input xor gates output to a z gate.
            If it does not, find the associated and_0 to swap with.

            Args:
                gates: Mapping from output gates to the input nodes and operation.
                result: The set of nodes that are invalid.
                bit_count: The bit count of the largest z state.
            """
            for gate, (x, op, _) in gates.items():
                if (
                    op != "XOR"
                    or x[0] not in "xy"
                    or gate in result
                    or gate == "z00"
                ):
                    continue

                if any(
                    (next_gate := gates[next_node])[1] == "XOR"
                    and next_gate[0] not in "xy"
                    for next_node in edges[gate]
                ):
                    continue

                result.add(gate)

                # Find the and_0 gate
                correct_z_gate = f"z{x[1:]}"
                a, _, b = gates[correct_z_gate]
                result.add(a if gates[a][1] == "AND" else b)

        result = set()
        check_xor_gates(gates, result)
        check_z_gates(gates, result, bit_count)
        check_in_xor_outputs_to_z_gates(gates, result)

        return ",".join(sorted(result))
