import numpy as np
from gym.spaces import Discrete


class Array(Discrete):
    def __init__(self, n, high=None, low=None):
        if max is None or min is None:
            raise ValueError("missing max and min")
        self.high = high
        self.low = low
        Discrete.__init__(self, n)
        self.shape = (50,)

    def sample(self):
        value = self.np_random.randint(low=self.low, high=self.high)
        pos = self.np_random.randint(self.n)
        sample = np.zeros(self.n)
        sample[pos] = value
        return sample
