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