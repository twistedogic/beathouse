import unittest
import gym
import src.beathouse


class TestSicBoRegister(unittest.TestCase):
    def setUp(self):
        env_name = "sic_bo-v0"
        self.env = gym.make(env_name)

    def test_spaces(self):
        assert 50 == self.env.action_space.n
        assert 2 == self.env.observation_space.n

    def test_step(self):
        actions = self.env.action_space.n
        obs, reward, done, info = self.env.step([0] * actions)
        assert reward == 0
        assert done == False
        assert len(info) == 0
        assert len(obs) == 2
