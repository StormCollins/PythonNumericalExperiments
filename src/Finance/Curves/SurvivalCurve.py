import matplotlib.pyplot as plt
import numpy as np


class SurvivalCurve:
    def __init__(self, tenors, probabilities_of_default, recovery_rate):
        self.tenors = tenors
        self.probabilities_of_default = probabilities_of_default
        self.recovery_rate = recovery_rate
        if not self.tenors.__contains__(0.0):
            self.tenors = np.append(0, self.tenors)
            self.probabilities_of_default = np.append(0, self.probabilities_of_default)

    def get_probabilities_of_default(self, interpolation_tenors):
        # linear interpolation with flat extrapolation
        # y = (y[i+1] - y[i])/(x[i+1] - x[i]) * (x - x[i]) + y[i]
        return np.interp(interpolation_tenors, self.tenors, self.probabilities_of_default)

    def get_hazard_rate(self, interpolation_tenors):
        pd = self.get_probability_of_default(interpolation_tenors)
        return -np.log(pd) / interpolation_tenors

    def plot_curve(self, values_to_plot='probabilities_of_default'):
        if values_to_plot.lower() == 'probabilities_of_default':
            plt.plot(self.tenors, self.probabilities_of_default)
        plt.show()

