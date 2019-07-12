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

    def get_zero_rates(self, tenors, rate_convention):
        discount_factors = self.get_discount_factors(tenors)
        if rate_convention == RateConvention.NACC:
            return -np.log(discount_factors) / tenors
        elif rate_convention == RateConvention.NACS:
            # df = (1 + r/2)^(2t)
            # r = 2*[df^(-1/2t) - 1]
            return 2*(discount_factors**(-1/(2*tenors)) - 1)
        elif rate_convention == RateConvention.NACM:
            # df = (1 + r/2)^(2t)
            # r = 2*[df^(-1/2t) - 1]
            return 12*(discount_factors**(-1/(12*tenors)) - 1)
        elif rate_convention == RateConvention.NACA:
            # df = (1 + r/2)^(2t)
            # r = 2*[df^(-1/2t) - 1]
            return discount_factors**(-1/tenors) - 1
        elif rate_convention == RateConvention.NACQ:
            # df = (1 + r/2)^(2t)
            # r = 2*[df^(-1/2t) - 1]
            return 4*(discount_factors**(-1/(4*tenors)) - 1)
        else:
            return "Invalid rate convention"
