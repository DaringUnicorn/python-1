# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


data = pd.read_csv("wine.csv")

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

standardScaler = StandardScaler(with_mean=False)
X_train = standardScaler.fit_transform(x_train)
X_test = standardScaler.transform(x_test)


from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_train2 = pca.fit_transform(X_train)

X_test2 = pca.transform(X_test)

from sklearn.linear_model import LogisticRegression


logisticRegression = LogisticRegression(random_state=0)
logisticRegression.fit(X_train2, y_train)


logisticRegression2 = LogisticRegression(random_state=0)
logisticRegression2.fit(X_train, y_train)


y_prediction = logisticRegression.predict(X_test)

y_prediction2 = logisticRegression.predict(X_test2)



from sklearn.metrics import confusion_matrix

confusionMatrix = confusion_matrix(y_test, y_prediction)
print(confusionMatrix)


confusionMatrix = confusion_matrix(y_test, y_prediction2)
print(confusionMatrix)



confusionMatrix = confusion_matrix(y_prediction, y_prediction2)
print(confusionMatrix)


from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

lda = LDA(n_components=2)

X_train_LDA = lda.fit_transform(X_train, y_train)
X_test_LDA = lda.transform(X_test)

logisticRegressionLda = LogisticRegression(random_state=0)
logisticRegressionLda.fit(X_train_LDA,y_train)


y_prediction_LDA = logisticRegressionLda.predict(X_test_LDA)

print("lda ve orijinal")

confusionMatrix4 = confusion_matrix(y_prediction, y_prediction_LDA)

print(confusionMatrix4)








