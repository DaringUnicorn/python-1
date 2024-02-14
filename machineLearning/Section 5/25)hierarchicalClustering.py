import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("musteriler.csv")

X = data.iloc[:,3:]

from sklearn.cluster import KMeans

kMeans = KMeans(n_clusters=3, init = "k-means++")

kMeans.fit(X)

clusterCenters = kMeans.cluster_centers_

results = []
for i in range(1,10):
    kMeans = KMeans(n_clusters=i, init="k-means++", random_state=123)
    kMeans.fit(X)
    results.append(kMeans.inertia_) #WCSS değerlerini iifade eder .inertia_
    
plt.plot(range(1,10),results)
plt.show()

kMeans = KMeans(n_clusters=4, init="k-means++",random_state=123)
Y_prediction = kMeans.fit_predict(X)
# Find indices for each cluster
cluster_0_indices = np.where(Y_prediction == 0)[0]
cluster_1_indices = np.where(Y_prediction == 1)[0]
cluster_2_indices = np.where(Y_prediction == 2)[0]

# Plot points for each cluster
plt.scatter(X.iloc[cluster_0_indices, 0], X.iloc[cluster_0_indices, 1], s=100, c="red")
plt.scatter(X.iloc[cluster_1_indices, 0], X.iloc[cluster_1_indices, 1], s=100, c="blue")
plt.scatter(X.iloc[cluster_2_indices, 0], X.iloc[cluster_2_indices, 1], s=100, c="green")
plt.title("K-Means")
plt.show()

from sklearn.cluster import AgglomerativeClustering

agglomerativeClustering = AgglomerativeClustering(n_clusters=3, affinity="euclidean", linkage="ward")

Y_prediction = agglomerativeClustering.fit_predict(X)

cluster_0_indices = np.where(Y_prediction == 0)[0]
cluster_1_indices = np.where(Y_prediction == 1)[0]
cluster_2_indices = np.where(Y_prediction == 2)[0]

# Plot points for each cluster
plt.scatter(X.iloc[cluster_0_indices, 0], X.iloc[cluster_0_indices, 1], s=100, c="red")
plt.scatter(X.iloc[cluster_1_indices, 0], X.iloc[cluster_1_indices, 1], s=100, c="blue")
plt.scatter(X.iloc[cluster_2_indices, 0], X.iloc[cluster_2_indices, 1], s=100, c="green")
plt.title("Hierarchical Clustering")

plt.show()


import scipy.cluster.hierarchy as sch

dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))


