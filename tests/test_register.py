import unittest
import gym
import src.beathouse 

class TestRegister(unittest.TestCase):
    def test_register(self):
        env_name = "sic_bo-v0"
        gym.make(env_name)
