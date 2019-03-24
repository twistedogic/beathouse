import unittest
import src.beathouse.env.sampler as sampler
import src.beathouse.env.bankroll as bankroll

class TestSampler(unittest.TestCase):
    def test_dice(self):
        num = 3
        output = sampler.dice(num)
        assert len(output) == num
        for n in output:
            assert 1 <= n <= 6

class TestBankroll(unittest.TestCase):
    def test_init(self):
        account = bankroll.Bankroll(start=100)
        expect = [100]
        self.assertListEqual(account.history, expect)

    def test_update(self):
        account = bankroll.Bankroll(start=100)
        expect = [100, 90, 190]
        account.update(-10)
        account.update(100)
        self.assertListEqual(account.history, expect)

    def test_reset(self):
        account = bankroll.Bankroll(start=100)
        expect = [100]
        account.update(-10)
        account.reset()
        self.assertListEqual(account.history, expect)
        

