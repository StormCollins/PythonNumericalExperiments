import numpy as np
from StochasticProcesses.GBM import GBM


class AsianOption:
    # assuming averaging period lasts till maturity
    def __init__(self, initial_value, strike, drift, volatility, T, averaging_period_start):
        self.S0 = initial_value
        self.K = strike
        self.mu = drift
        self.sigma = volatility
        self.T = T
        self.T_avg_start = averaging_period_start

    def monte_carlo_price(self, simulation_count, time_step_size):
        gbm = GBM(self.S0, self.mu, self.sigma, time_step_size, self.T, simulation_count)
        gbm.generate_paths()
        time_steps = gbm.get_time_steps()
        T_avg_start_index = np.where(time_steps >= self.T_avg_start)[0][0]
        prices = np.mean(gbm.paths[:, T_avg_start_index:], 1)
        prices = np.exp(-self.mu*self.T)*np.maximum(prices - self.K, 0)
        price = np.mean(prices)
        stddev = np.std(prices) / np.sqrt(simulation_count)
        return [price, stddev]