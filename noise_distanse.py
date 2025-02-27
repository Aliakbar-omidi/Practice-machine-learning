import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs


data, label = make_blobs(n_samples=300, centers=3, n_features=3, cluster_std=3.5)

data = data[label == 0]

center = np.mean(data, axis=0)

x, y, z = data[:, 0], data[:, 1], data[:, 2]

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(*center, c="black")

std = np.std(data)
mean = np.mean(data)

normal_data = []
noisy_data = []

for p in data:
    distance = np.sqrt((p[0] - center[0]) ** 2 + (p[1] - center[1]) ** 2 + (p[2] - center[2]) ** 2)
    if distance < mean + std * 1.5:
        ax.plot([p[0], center[0]], [p[1], center[1]], [p[2], center[2]], "b--")
        ax.scatter(*p, c="green")
        normal_data.append(p)
    else:
        ax.scatter(*p, c="red")
        noisy_data.append(p)

plt.show()
