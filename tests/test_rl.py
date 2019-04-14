import pytest
import unittest
import numpy as np
import gym
import src.beathouse



@pytest.mark.skip()
class TestRL(unittest.TestCase):
    def setUp(self):
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense, Activation, Flatten
        from tensorflow.keras.optimizers import Adam

        from rl.agents.cem import CEMAgent
        from rl.memory import EpisodeParameterMemory
        from rl.core import Processor
        
        class EnvProcessor(Processor):
            def process_observation(self, observation):
                return np.array(observation)

        ENV_NAME = "sic_bo-v0"
        env = gym.make(ENV_NAME)

        np.random.seed(123)
        env.seed(123)

        nb_actions = env.action_space.n

        # Option 1 : Simple model
        model = Sequential()
        model.add(Flatten(input_shape=(1,)))
        model.add(Dense(nb_actions))
        model.add(Activation("relu"))

        memory = EpisodeParameterMemory(limit=1000, window_length=1)

        cem = CEMAgent(
            model=model,
            nb_actions=nb_actions,
            memory=memory,
            batch_size=50,
            nb_steps_warmup=2000,
            train_interval=50,
            elite_frac=0.05,
            processor=EnvProcessor(),
        )
        cem.compile()
        self.cem = cem
        self.env = env

    def test_fit(self):
        self.cem.fit(self.env, nb_steps=2, visualize=False, verbose=2)
        self.cem.test(self.env, nb_episodes=5, visualize=False)
        assert len(self.env.history) == 2
