import gym
from gym import error, spaces, utils
from gym.utils import seeding
from .sic_bo_odd import Game
from .sic_bo_sampler import dice
from ..base import Bankroll


class SicBoEnv(gym.Env, Game, Bankroll):
    metadata = {"render.modes": ["human"]}

    def __init__(self, start=1000, min_bet=200, max_bet=1000):
        Bankroll.__init__(self, start=start)
        Game.__init__(self)
        self.dice = dice
        self.min_bet = min_bet
        self.max_bet = max_bet
        self._action_set = sorted(list(self.states.keys()))

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
    def _profit_and_loss(bets, payout):
        profit = sum([bets.get(k, 0) * v for k, v in payout.items()])
        loss = sum([v for k, v in bets.items() if payout.get(k, None)])
        return profit - loss

    def step(self, action):
        bets = self._action_to_bets(action)
        if self._bet_size(bets) > self.balance:
            # todo
            return 0, -self.balance
        outcome = dice(3)
        payout = self.game.evaluate(outcome)
        reward = self._profit_and_loss(bets, payout)
        return (self.balance,)

    def _done(self):
        return self.balance < self.min_bet
