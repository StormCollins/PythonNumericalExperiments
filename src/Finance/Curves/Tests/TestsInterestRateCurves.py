import numpy as np

from src.Finance.Curves.InterestRateCurve import InterestRateCurve
from src.Finance.Curves.RateConvention import RateConvention

import unittest


class TestsInterestRateCurves(unittest.TestCase):
    def test_discount_factor_interpolation(self):
        interest_rate_curve = InterestRateCurve(np.array([0.25, 0.5, 0.75, 1.0]), np.array([0.9, 0.85, 0.8, 0.75]))
        actual_discount_factors\
            = interest_rate_curve.get_discount_factors(np.array([0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]))
        expected_discount_factors = np.array([0.9, 0.875, 0.85, 0.825, 0.8, 0.775, 0.75])
        np.testing.assert_array_almost_equal(expected_discount_factors, actual_discount_factors, 2)