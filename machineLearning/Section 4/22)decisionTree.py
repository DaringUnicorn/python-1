import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("veriler.csv")

x = dataFrame.iloc[:,1:4].values
y = dataFrame.iloc[:,-1].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler

standardScaler = StandardScaler()

X_train = standardScaler.fit_transform(x_train)
X_test = standardScaler.transform(x_test)


from sklearn.tree import DecisionTreeClassifier

decisionTreeClassifier = DecisionTreeClassifier(criterion = "entropy")
decisionTreeClassifier.fit(X_train, y_train)


y_prediction = decisionTreeClassifier.predict(X_test)

from sklearn.metrics import confusion_matrix

confusionMatrix = confusion_matrix(y_test, y_prediction)























































