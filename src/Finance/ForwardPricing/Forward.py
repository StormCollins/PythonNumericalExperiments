import numpy as np

from src.Finance.Enums.LongShort import LongShort
from src.Finance.StochasticProcesses.GBM import GBM


class Forward:
    # The volatility is only needed if pricing via Monte Carlo
    def __init__(self, initial_value, strike, drift, tenor, volatility=0, long_short=LongShort.LONG):
        self.initial_value = initial_value
        self.strike = strike
        self.drift = drift
        self.tenor = tenor
        self.volatility = volatility
        self.long_short = long_short

    def price(self):
        if self.long_short == LongShort.LONG:
            return self.initial_value * np.exp(self.drift * self.tenor) - self.strike
        else:
            return self.strike - self.initial_value * np.exp(self.drift * self.tenor)

    def monte_carlo_price(self, time_step_size, simulation_count, return_price_paths=False):
        gbm = GBM(self.S0, self.mu, self.sigma, self.T, time_step_size, simulation_count)
        gbm.generate_paths()
        if self.long_short == LongShort.LONG:
            prices = np.exp(-self.mu * self.T) \
               * (gbm.paths[:, -1] - self.K)
        else:
            prices = np.exp(-self.mu * self.T) \
                * (self.K - gbm.paths[:, -1])
        if return_price_paths:
            return prices
        else:
            price = np.mean(prices)
            stddev = np.std(prices)/np.sqrt(simulation_count)
            return [price, stddev]
