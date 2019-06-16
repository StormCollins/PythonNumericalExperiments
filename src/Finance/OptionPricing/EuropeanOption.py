from StochasticProcesses.GBM import GBM
import numpy as np
from scipy.stats import norm


# assume a call for now
class EuropeanOption:
    def __init__(self, initial_value, strike, drift, volatility, T):
        self.S0 = initial_value
        self.K = strike
        self.mu = drift
        self.sigma = volatility
        self.T = T

    def black_scholes_price(self):
        d1 = (np.log(self.S0/self.K) + (self.mu - 0.5*self.sigma**2)*self.T)\
             /(self.sigma*np.sqrt(self.T))
        d2 = d1 - self.sigma*np.sqrt(self.T)
        return self.S0*norm.cdf(d1) - self.K*np.exp(-self.mu*self.T)*norm.cdf(d2)

    def monte_carlo_price(self, simulation_count, time_step_size):
        gbm = GBM(self.S0, self.mu, self.sigma, time_step_size, self.T, simulation_count)
        gbm.generate_paths()
        return np.maximum(np.mean(gbm.paths) - self.K, 0)
