import numpy as np

from src.Finance.Enums.LongShort import LongShort

class Forward:
    # The volatility is only needed if pricing via Monte Carlo
    def __init__(self, initial_value, strike, drift, tenor, volatility = 0):
        self.initial_value = initial_value
        self.strike = strike
        self.drift = drift
        self.tenor = tenor
        self.volatility = volatility

    def price(self, long_short):
        if long_short == LongShort.Long:
            return self.initial_value * np.exp(self.drift * self.tenor) - self.strike
        else:
            return self.strike - self.initial_value * np.exp(self.drift * self.tenor)

