import numpy as np
import random
import copy
from .bitstring import *

class MonteCarlo:
    def __init__(self, ham, seed=42):
        self.ham = ham
        self.length = ham.length
        self.config = BitString(self.length)
        random.seed(seed)

    def run(self, T=2.0, n_samples=100000, n_burn=100):
        E_samples = []
        M_samples = []

        for step in range(n_samples + n_burn):
            for n in range(self.length):
                new_config = copy.deepcopy(self.config)
                new_config.flip_site(n)

                E_old = self.ham.energy(self.config)
                E_new = self.ham.energy(new_config)

                dE = E_new - E_old
                accept_prob = 1.0 if dE <= 0 else np.exp(-dE / T)

                if random.random() < accept_prob:
                    self.config = new_config

            if step >= n_burn:
                E_samples.append(self.ham.energy(self.config))
                M_samples.append(self.config.on() - self.config.off())

        return E_samples, M_samples
