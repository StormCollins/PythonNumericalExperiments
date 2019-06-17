import unittest

from OptionPricing.AsianOption import AsianOption
from OptionPricing.OptionStyle import OptionStyle

# Asian option price example taken from :
# Numerical Methods in Finance & Economics by Paolo Brandimarte pg 456


# TODO: asian should be cheaper than European;
# TODO: asian volatility should be lower than European
class TestsAsianOption(unittest.TestCase):
    def test_monte_carlo_call_pricing(self):
        option = AsianOption(50, 52, 0.1, 0.4, 5/12, 0.2)
        [price, stddev] = option.monte_carlo_price(1000, 5/(10*12))
        self.assertTrue(3.9605 - 2*stddev < price < 3.9605 + 2*stddev)
