import numpy as np

class InterestRateCurve:
    def __init__(self, tenors, discount_factors):
        self.tenors = tenors
        self.discount_factors = discount_factors

    def get_discount_factors(self, tenors):
        return np.interp(tenors, self.tenors, self.discount_factors)