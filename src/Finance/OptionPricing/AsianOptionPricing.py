import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Initial inputs
S0 = 100
mu = 0.1
sigma = 0.2
dt = 0.01
T = 1
time_step_count = np.int(T/dt)
simulation_count = 100


S0_vec = np.repeat(S0, simulation_count)[np.newaxis].T

S = np.zeros([simulation_count, time_step_count]);
S[:, 0] = S0
for i in range(1, time_step_count):
    Z = np.random.standard_normal(simulation_count)
    S[:, i] = S[:, i - 1] \
              * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

sorted_indices_of_averages = np.argsort(np.average(S, 1))
sorted_S = S[sorted_indices_of_averages].T



t = np.linspace(0, T, time_step_count)
sns.set_palette(sns.cubehelix_palette(simulation_count, start=.5, rot=-.75))
plt.plot(t, sorted_S)
plt.show()