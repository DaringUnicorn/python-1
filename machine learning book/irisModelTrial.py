import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

# print(iris["DESCR"])
# print(iris["target_names"])
# print(iris["feature_names"])

x_train, x_test, y_train, y_test = train_test_split(iris["data"], iris["target"], random_state=0)

figure, axes = plt.subplots(3, 3, figsize= (10,10))


for i in range(3):
    for j in range(3):
        axes[i, j].scatter(x_train[:,j], x_train[:, i + 1], c= y_train, s=60)
        axes[i, j].set_xticks(())
        axes[i, j].set_yticks(())
        if i == 2:
            axes[i, j].set_xlabel(iris["feature_names"][j])
        if j == 0:
            axes[i, j].set_ylabel(iris["feature_names"][i + 1])

        if j > i:
            axes[i, j].set_visible(False)

# plt.show()

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train, y_train)

KNeighborsClassifier(algorithm="auto", leaf_size=30, metric="minkowski",
                     metric_params=None, n_jobs=1, n_neighbors=1, p=2,
                     weights="uniform")

x_new = np.array([[5,2.9,1,0.2]])

prediction = knn.predict(x_new)

new = iris["target_names"][prediction]

print(new)


y_prediction = knn.predict(x_test)

print(np.mean(y_test == y_prediction))
print(knn.score(x_test, y_test))