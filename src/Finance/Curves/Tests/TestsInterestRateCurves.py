import numpy as np

from src.Finance.Curves.InterestRateCurve import InterestRateCurve
from src.Finance.Curves.RateConvention import RateConvention

import unittest


class TestsInterestRateCurves(unittest.TestCase):
    def test_discount_factor_interpolation(self):
        interest_rate_curve\
            = InterestRateCurve(np.array([0.25, 0.5, 0.75, 1.0]), np.array([0.9, 0.85, 0.8, 0.75]))
        actual_discount_factors\
            = interest_rate_curve.get_discount_factors(
                np.array([0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]))
        expected_discount_factors = np.array([0.95, 0.9, 0.875, 0.85, 0.825, 0.8, 0.775, 0.75])
        np.testing.assert_array_almost_equal(expected_discount_factors, actual_discount_factors, 2)

    def test_discount_factor_extrapolation(self):
        interest_rate_curve\
            = InterestRateCurve(np.array([0.25, 0.5, 0.75, 1.0]), np.array([0.9, 0.85, 0.8, 0.75]))
        actual_discount_factors\
            = interest_rate_curve.get_discount_factors(np.array([2.0]))
        expected_discount_factors = np.array([0.75])
        np.testing.assert_array_almost_equal(expected_discount_factors, actual_discount_factors, 2)

    def test_nacc_zero_rates_without_interpolation(self):
        tenors = np.array([0.25, 0.5, 0.75, 1.0])
        expected_rates = np.array([0.1, 0.11, 0.12, 0.13])
        discount_factors = np.exp(-tenors * expected_rates)
        interest_rate_curve = InterestRateCurve(tenors, discount_factors)
        actual_rates = interest_rate_curve.get_zero_rates(tenors, RateConvention.NACC)
        np.testing.assert_array_almost_equal(expected_rates, actual_rates, 2)

    def test_nacm_zero_rates_without_interpolation(self):
        tenors = np.array([0.25, 0.5, 0.75, 1.0])
        expected_rates = np.array([0.1, 0.11, 0.12, 0.13])
        discount_factors = (1 + expected_rates/12)**(-12*tenors)
        interest_rate_curve = InterestRateCurve(tenors, discount_factors)
        actual_rates = interest_rate_curve.get_zero_rates(tenors, RateConvention.NACA)
        np.testing.assert_array_almost_equal(expected_rates, actual_rates, 2)

    def test_nacq_zero_rates_without_interpolation(self):
        tenors = np.array([0.25, 0.5, 0.75, 1.0])
        expected_rates = np.array([0.1, 0.11, 0.12, 0.13])
        discount_factors = (1 + expected_rates/4)**(-4*tenors)
        interest_rate_curve = InterestRateCurve(tenors, discount_factors)
        actual_rates = interest_rate_curve.get_zero_rates(tenors, RateConvention.NACA)
        np.testing.assert_array_almost_equal(expected_rates, actual_rates, 2)

    def test_nacs_zero_rates_without_interpolation(self):
        tenors = np.array([0.25, 0.5, 0.75, 1.0])
        expected_rates = np.array([0.1, 0.11, 0.12, 0.13])
        discount_factors = (1 + expected_rates/2)**(-2*tenors)
        interest_rate_curve = InterestRateCurve(tenors, discount_factors)
        actual_rates = interest_rate_curve.get_zero_rates(tenors, RateConvention.NACA)
        np.testing.assert_array_almost_equal(expected_rates, actual_rates, 2)

    def test_naca_zero_rates_without_interpolation(self):
        tenors = np.array([0.25, 0.5, 0.75, 1.0])
        expected_rates = np.array([0.1, 0.11, 0.12, 0.13])
        discount_factors = (1 + expected_rates)**(-1*tenors)
        interest_rate_curve = InterestRateCurve(tenors, discount_factors)
        actual_rates = interest_rate_curve.get_zero_rates(tenors, RateConvention.NACA)
        np.testing.assert_array_almost_equal(expected_rates, actual_rates, 2)


