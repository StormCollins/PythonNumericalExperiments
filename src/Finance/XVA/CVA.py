from src.Finance.Curves.SurvivalCurve import SurvivalCurve

import numpy as np

class CVA:
    def __init__(self, survival_curve):
        self.survival_curve = survival_curve

    def compute_cva(self, price_paths):
        np.maximum(price_paths, 0)