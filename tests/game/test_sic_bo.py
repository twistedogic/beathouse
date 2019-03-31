import unittest
from src.beathouse.env.game import sic_bo


class TestSicBo(unittest.TestCase):
    def test_triple(self):
        cases = [
            dict(val=3, out=[3, 3, 3], expect=True),
            dict(val=2, out=[2, 2, 3], expect=False),
            dict(val=1, out=[1, 1, 1], expect=True),
        ]
        for case in cases:
            val = case.get("val")
            out = case.get("out")
            expect = case.get("expect")
            assert sic_bo.is_triple(val)(out) == expect

    def test_count(self):
        cases = [
            dict(val=1, out=[1, 2, 3], expect=1),
            dict(val=2, out=[1, 2, 3], expect=1),
            dict(val=1, out=[1, 1, 3], expect=2),
            dict(val=1, out=[3, 3, 3], expect=0),
            dict(val=3, out=[3, 3, 3], expect=3),
        ]
        for case in cases:
            val = case.get("val")
            out = case.get("out")
            expect = case.get("expect")
            assert sic_bo.count(val)(out) == expect

    def test_specific_two(self):
        cases = [
            dict(a=1, b=2, out=[1, 2, 3], expect=True),
            dict(a=1, b=2, out=[1, 1, 1], expect=False),
            dict(a=1, b=3, out=[1, 2, 3], expect=True),
        ]
        for case in cases:
            a = case.get("a")
            b = case.get("b")
            out = case.get("out")
            expect = case.get("expect")
            assert sic_bo.specific_two(a, b)(out) == expect

    def test_value_bets(self):
        bets = [(4, 10)]
        test_input = [1, 1, 2]
        out = sic_bo.value_bets(bets)
        output = dict()
        for k, v in out.items():
            if v.func(test_input):
                output[k] = v.payout
        expect = dict(value_4=10)
        self.assertEqual(output, expect)

    def test_payout(self):
        payout = sic_bo.payout()
        test = payout.get("triple_1")
        assert test.func([1, 1, 1])


class TestSicBoGame(unittest.TestCase):
    def setUp(self):
        self.game = sic_bo.Game()

    def test_triple(self):
        out = self.game.evaluate([1, 1, 1])
        expect = dict(triple_1=150, triple_any=24)
        self.assertEqual(out, expect)

    def test_double(self):
        out = self.game.evaluate([1, 1, 3])
        expect = dict(
            double_1=8, small=1, combination_1_3=5, single_1=1, single_3=1, value_5=18
        )
        self.assertEqual(out, expect)

    def test_combinations(self):
        out = self.game.evaluate([1, 2, 3])
        expect = dict(
            small=1,
            value_6=14,
            single_1=1,
            single_2=1,
            single_3=1,
            combination_1_2=5,
            combination_1_3=5,
            combination_2_3=5,
        )
        self.assertEqual(out, expect)
