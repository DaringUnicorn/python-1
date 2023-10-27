import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


data = pd.read_csv(r"C:/Users/Ayhan/Desktop/ml/section-3/values.csv")

print(data)


gender = data.iloc[:,4:].values

print(gender)

labelEncoder = LabelEncoder()

gender[:,0] = labelEncoder.fit_transform(data.iloc[:,4])

print(gender)

ohe = OneHotEncoder()

gender = ohe.fit_transform(gender).toarray()

print(gender.shape)


genderDataframe = pd.DataFrame(data=gender, index= range(22), columns= ["male", "female"] )

print(genderDataframe)


data.drop(columns="cinsiyet", inplace=True, axis=1)

print(data)


data = pd.concat([data, genderDataframe], axis=1)

print("data\n", data)