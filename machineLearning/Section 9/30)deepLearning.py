import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


data = pd.read_csv("customerChurnAnalysis.csv")

X = data.iloc[:,3:].values
Y = data.iloc[:,13].values

labelEncoder = LabelEncoder()

X[:,1] = labelEncoder.fit_transform(X[:,1])


labelEncoder2 = LabelEncoder()

X[:,2] = labelEncoder2.fit_transform(X[:,2])


#ohe = ColumnTransformer(["ohe", OneHotEncoder(dtype=float),[1]], remainder="passthrough")
ohe = ColumnTransformer(transformers=[("ohe", OneHotEncoder(dtype=float), [1])], remainder="passthrough")

X = ohe.fit_transform(X)
X = X[:,1:]

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.33,random_state=0)

standardScaler = StandardScaler()
X_train = standardScaler.fit_transform(x_train)
X_test = standardScaler.fit_transform(x_test)



from keras.models import Sequential
from keras.layers import Dense


sequential = Sequential()

#sequential.add(Dense(6, init = "uniform" , activation = "relu", input_dim = 11))
sequential.add(Dense(6, kernel_initializer="uniform", activation="relu", input_dim=11))

sequential.add(Dense(6, kernel_initializer="uniform", activation="relu"))

sequential.add(Dense(1, kernel_initializer="uniform", activation="sigmoid"))

sequential.compile(optimizer="adam", loss = "binary_crossentropy", metrics = ["accuracy"])

sequential.fit(X_train, y_train, epochs=50)

y_prediction = sequential.predict(X_test)


y_prediction = (y_prediction > 0.50)


from sklearn.metrics import confusion_matrix

confusionMatrix = confusion_matrix(y_test, y_prediction)


