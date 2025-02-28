import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

x, y = make_blobs(n_samples=300, centers=3, n_features=2, cluster_std=2)


plt.subplot(1, 2, 1)
plt.scatter(x[:, 0], x[:, 1], c=y)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(x, y)
y_pred = model.predict(x)
print(classification_report(y, y_pred))


plt.subplot(1, 2, 2)
plt.scatter(x[:, 0], x[:, 1], c=y_pred)

point = np.array([[0, 0]])

plt.scatter(point[:, 0], point[:, 1], c='red', label='point')
y_pred = model.predict(point)
y_pred_proba = model.predict_proba(point)
print("predict point: ", y_pred)
print("predict proba: ", y_pred_proba)

plt.legend()
plt.show()
