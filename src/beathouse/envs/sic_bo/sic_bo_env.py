import gym
from gym import error, spaces, utils
from gym.utils import seeding
from numpy import std
from .sic_bo_odd import Game
from ..base import Bankroll
from ..spaces import Array


class SicBoEnv(Bankroll, gym.Env, Game):
    metadata = {"render.modes": ["human"]}

    def __init__(self, start=1000, min_bet=200, max_bet=1000):
        Bankroll.__init__(self, start=start)
        Game.__init__(self)
        self.seed()
        self.min_bet = min_bet
        self.max_bet = max_bet
        self._action_set = sorted(list(self.states.keys()))
        self.action_space = Array(len(self._action_set), high=max_bet, low=min_bet)
        self.observation_space = spaces.Discrete(2)
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return seed

    def _dice(self, num=3):
        return self.np_random.randint(1, high=7, size=num)

    def render(self, mode="human", close=False):
        pass

    def _action_to_bets(self, actions):
        return dict(
            [
                (self._action_set[i], v if v <= self.max_bet else self.max_bet)
                for i, v in enumerate(actions)
                if v >= self.min_bet
            ]
        )

    @staticmethod
    def _bet_size(bets):
        return sum(bets.values())

    @staticmethod
    def _reward(bets, payout):
        profit = sum([bets.get(k, 0) * v for k, v in payout.items()])
        loss = sum([v for k, v in bets.items() if payout.get(k, None)])
        return profit - loss

    def _get_obs(self):
        return [self.balance, std(self.history)]

    def _done(self):
        return self.balance < self.min_bet

    def step(self, action):
        info = {}
        bets = self._action_to_bets(action)
        if self._bet_size(bets) > self.balance:
            return self._get_obs(), -self._bet_size(bets), True, info
        outcome = self._dice()
        payout = self.evaluate(outcome)
        reward = self._reward(bets, payout)
        return self._get_obs(), reward, self._done(), info

    def reset(self):
        self._reset()
        return self._get_obs(), 0, self._done(), {}
