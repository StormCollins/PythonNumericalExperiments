import matplotlib.pyplot as plt
import numpy as np

S0 = 100.0
r = 0.1
sigma = 0.2
T = 1.0  # 1 year
dT = 0.1
N = 100  # number of paths


S_paths = np.zeros((N, np.int(T/dT)))
S_paths[:, 0] = np.repeat(S0, N)
for i in range(1, 10):
    random_vector = np.random.normal(0, 1, N)
    S_paths[:, i] = S_paths[:, i - 1] * np.exp((r - 0.5 * sigma ** 2) * dT + sigma * random_vector * np.sqrt(dT))

# for i in range(0, len(S_paths[0, :])):
#     print(S_paths[0, i])
t = np.arange(0, T, dT)
plt.plot(t, S_paths.T)
plt.show()