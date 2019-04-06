import unittest
from src.beathouse.envs.sic_bo import sic_bo_odd
from src.beathouse.envs.sic_bo import sic_bo_sampler
from src.beathouse.envs.sic_bo import sic_bo_env


class TestSicBoSampler(unittest.TestCase):
    def test_dice(self):
        num = 3
        out = sic_bo_sampler.dice(num)
        assert len(out) == num
        assert all([1 <= i <= 6 for i in out])


class TestSicBoOdd(unittest.TestCase):
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
            assert sic_bo_odd.is_triple(val)(out) == expect

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
            assert sic_bo_odd.count(val)(out) == expect

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
            assert sic_bo_odd.specific_two(a, b)(out) == expect

    def test_value_bets(self):
        bets = [(4, 10)]
        test_input = [1, 1, 2]
        out = sic_bo_odd.value_bets(bets)
        output = dict()
        for k, v in out.items():
            if v.func(test_input):
                output[k] = v.payout
        expect = dict(value_4=10)
        self.assertEqual(output, expect)

    def test_payout(self):
        payout = sic_bo_odd.payout()
        test = payout.get("triple_1")
        assert test.func([1, 1, 1])


class TestSicBoGame(unittest.TestCase):
    def setUp(self):
        self.game = sic_bo_odd.Game()

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


class TestSicBoEnv(unittest.TestCase):
    def setUp(self):
        start = 1000
        min_bet = 100
        max_bet = 1000
        self.env = sic_bo_env.SicBoEnv()
