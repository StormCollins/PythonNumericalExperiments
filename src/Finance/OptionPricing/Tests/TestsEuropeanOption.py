from OptionPricing.EuropeanOption import EuropeanOption
import unittest


class TestsEuropeanOption(unittest.TestCase):
    def test_basic_black_scholes(self):
        option = EuropeanOption(50, 52, 0.1, 0.4, 5/12)
        print(f"European option price {option.black_scholes_price()}")
        self.assertAlmostEqual(option.black_scholes_price(), 5.1911, 4)
