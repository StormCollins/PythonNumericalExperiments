import unittest

from src.Finance.OptionPricing.EuropeanOption import EuropeanOption
from src.Finance.OptionPricing.OptionStyle import OptionStyle


class TestsCVA(unittest.TestCase):
    # the CVA on an option & a forward should be the same
    def test_option_and_forward_cva(self):
        european_option = EuropeanOption(100, 90, 0.1, 0.2, 1, OptionStyle.CALL)


    # CVA on something that is more positive should be higher