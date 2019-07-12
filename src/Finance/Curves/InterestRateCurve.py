import numpy as np

from src.Finance.Curves.RateConvention import RateConvention

class InterestRateCurve:
    def __init__(self, tenors, discount_factors):
        self.tenors = tenors
        self.discount_factors = discount_factors
        if not tenors.__contains__(0):
            self.tenors = np.append(0, self.tenors)
            self.discount_factors = np.append(1, self.discount_factors)

    def get_discount_factors(self, tenors):
        return np.interp(tenors, self.tenors, self.discount_factors)