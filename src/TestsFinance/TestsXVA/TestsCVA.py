import unittest

from src.Finance.XVA.CVA import CVA
from src.Finance.OptionPricing.EuropeanOption import EuropeanOption
from src.Finance.OptionPricing.OptionStyle import OptionStyle
from src.Finance.Curves.InterestRateCurve import InterestRateCurve


class TestsCVA(unittest.TestCase):
    # the CVA on an option & a forward should be the same
    def test_option_and_forward_cva(self):
        european_option = EuropeanOption(100, 90, 0.1, 0.2, 1, OptionStyle.CALL)
        price_paths = european_option.monte_carlo_price(10000, 0.5, True)
        ir_curve_zar = InterestRateCurve()
        cva = CVA()
        fxSpot = 14.139235
        fx1YVol = 0.1545
        fx2YVol = 0.1675

    # CVA on something that is more positive should be higher