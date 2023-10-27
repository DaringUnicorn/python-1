import pandas as pd
import numpy as np
from sklearn import preprocessing
import categoricValues
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x_train, x_test, y_train, y_test = train_test_split(categoricValues.s, categoricValues.result3, random_state=0)


sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transformt(x_test)

