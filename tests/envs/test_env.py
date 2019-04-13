import unittest
from src.beathouse.envs.base import Bankroll


class TestBankroll(unittest.TestCase):
    def test_init(self):
        account = Bankroll(start=100)
        expect = [100]
        self.assertListEqual(account.history, expect)

    def test_update(self):
        account = Bankroll(start=100)
        expect = [100, 90, 190]
        account.update(-10)
        account.update(100)
        self.assertListEqual(account.history, expect)

    def test_reset(self):
        account = Bankroll(start=100)
        expect = [100]
        account.update(-10)
        account._reset()
        self.assertListEqual(account.history, expect)
