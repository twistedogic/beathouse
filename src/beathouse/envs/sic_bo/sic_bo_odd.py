from enum import Enum
from ..state import State, Odd


def count(val):
    def f(out):
        return sum([1 for i in out if i == val])

    return f


def any_triples(out):
    return all([out[0] == i for i in out])


def is_big(out):
    return 11 < sum(out) < 17


def is_small(out):
    return 4 < sum(out) < 10


def is_total(val):
    def f(out):
        return val == sum(out)

    return f


def is_double(val):
    def f(out):
        return count(val)(out) >= 2

    return f


def is_triple(val):
    def f(out):
        return count(val)(out) == 3

    return f


def is_single(val):
    def f(out):
        return val in out

    return f


def specific_two(a, b):
    def f(out):
        return is_single(a)(out) and is_single(b)(out)

    return f


def value_bets(values):
    return dict(
        [("value_{}".format(v), State(payout, is_total(v))) for v, payout in values]
    )


def combination_bets(payout):
    return dict(
        [
            ("combination_{}_{}".format(a, b), State(payout, specific_two(a, b)))
            for a in range(1, 7)
            for b in range(1, 7)
            if a != b and not a > b
        ]
    )


def payout():
    other = dict(
        big=State(1, is_big),
        small=State(1, is_small),
        triple_any=State(24, any_triples),
    )
    triples = dict(
        [("triple_{}".format(i), State(150, is_triple(i))) for i in range(1, 7)]
    )
    doubles = dict(
        [("double_{}".format(i), State(8, is_double(i))) for i in range(1, 7)]
    )
    singles = dict(
        [("single_{}".format(i), State(1, is_single(i))) for i in range(1, 7)]
    )
    values = value_bets(
        [
            (4, 50),
            (5, 18),
            (6, 14),
            (7, 12),
            (8, 8),
            (9, 6),
            (10, 6),
            (17, 50),
            (16, 18),
            (15, 14),
            (14, 12),
            (13, 8),
            (12, 6),
            (11, 6),
        ]
    )
    combinations = combination_bets(5)
    return {**other, **triples, **doubles, **singles, **values, **combinations}


class Game(Odd):
    def __init__(self):
        self.states = payout()

    def evaluate(self, outcome):
        pay = self._evaluate(outcome)
        if pay.get("triple_any", None):
            return dict([(k, v) for k, v in pay.items() if "triple_" in k])
        return pay
