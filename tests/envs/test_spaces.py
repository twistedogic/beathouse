import unittest
from src.beathouse.envs import spaces


class TestArray(unittest.TestCase):
    def setUp(self):
        self.high = 100
        self.low = 10
        self.n = 50
        self.array = spaces.Array(self.n, high=self.high, low=self.low)

    def test_sample(self):
        sample = self.array.sample()
        bets = list(filter(lambda item: item != 0, sample))
        assert len(bets) == 1
        assert all(map(lambda item: item <= self.high, sample))
        assert len(sample) == self.n

    def test_n(self):
        assert self.array.n == self.n

    def test_shape(self):
        assert self.array.shape == (self.n,)
