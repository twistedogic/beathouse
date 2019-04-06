from collections import namedtuple
from abc import ABCMeta, abstractmethod

State = namedtuple("State", ["payout", "func"])


class Odd(metaclass=ABCMeta):
    """Odd evaluation
    
    states -- dict of State
    """

    def __init__(self, states):
        self.states = states

    def _evaluate(self, outcome):
        pay = dict()
        for k, v in self.states.items():
            payout, func = v
            if func(outcome):
                pay[k] = payout
        return pay

    @abstractmethod
    def evaluate(self, outcome):
        pass
