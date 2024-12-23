"""
Tests day 23 solver.
"""

from test.base_test import BaseTests

from advent_of_code_2024.day_23 import Solver


class TestDay23(BaseTests):
    """Tests the day 23 solver."""

    solver = Solver()
    cases = [
        (
            """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""",
            7,
            "co,de,ka,ta",
        )
    ]
