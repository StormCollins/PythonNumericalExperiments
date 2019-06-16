import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class GBM:
    def __init__(self, S0, mu, sigma, dt, T, simulation_count):
        self.S0 = S0
        self.mu = mu
        self.sigma = sigma
        self.dt = dt
        self.T = T
        self.time_step_count = np.int(self.T / self.dt)
        self.simulation_count = simulation_count
        self.S = []

    def GeneratePaths(self):
        self.S = np.zeros([self.simulation_count, self.time_step_count])
        self.S[:, 0] = self.S0
        for i in range(1, self.time_step_count):
            z = np.random.standard_normal(self.simulation_count)
            self.S[:, i] = self.S[:, i - 1] \
                      * np.exp((self.mu - 0.5 * self.sigma**2)
                               * self.dt + self.sigma * np.sqrt(self.dt) * z)

    def plot_paths(self):
        sorted_indices_of_averages = np.argsort(np.average(self.S, 1))
        sorted_S = self.S[sorted_indices_of_averages].T
        t = np.linspace(0, self.T, self.time_step_count)
        sns.set_palette(sns.cubehelix_palette(self.simulation_count, start=.5, rot=-.75))
        plt.plot(t, sorted_S)
        plt.show()
