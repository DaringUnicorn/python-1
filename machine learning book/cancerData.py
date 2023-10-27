import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer


cancer = load_breast_cancer()

print(cancer.keys())

print(cancer.data.shape)


print(cancer.target_names)

print(np.bincount(cancer.target))


print(cancer.feature_names)

print(cancer.DESCR)