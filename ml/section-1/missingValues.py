import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


data = pd.read_csv(r"C:/Users/Ayhan/Desktop/ml/missingDatas.csv")

imputer = SimpleImputer(missing_values= np.nan, strategy="mean")

age = data.iloc[:,1:4].values

imputer = imputer.fit(age[:,1:4])

age[:,1:4] = imputer.transform(age[:,1:4])

print(age)