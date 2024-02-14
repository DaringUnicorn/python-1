import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("ads.csv")

x = dataFrame.iloc[:,2:4].values
y = dataFrame.iloc[:,-1].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler

standardScaler = StandardScaler()

X_train = standardScaler.fit_transform(x_train)
X_test = standardScaler.transform(x_test)


from sklearn.svm import SVC

svc = SVC(kernel = "linear")

svc.fit(X_train, y_train)

y_prediction = svc.predict(X_test)

from sklearn.metrics import confusion_matrix

confusionMatrix = confusion_matrix(y_test, y_prediction)

print(confusionMatrix)

from sklearn.model_selection import cross_val_score, GridSearchCV

accuracy = cross_val_score(estimator = svc, X = X_train, y=y_train, cv=4)

print(accuracy.mean())

parameters = [{"C": [1,2,3,4,5], "kernel": ["linear"]},
              {"C": [1,10,100,1000], "kernel" : ["rbf"], "gamma" : [1, 0.5, 0.1, 0.01, 0.001]}]

gridSearch = GridSearchCV(estimator=svc, param_grid=parameters, scoring="accuracy", cv=10, n_jobs=-1)

gridSearchResult = gridSearch.fit(X_train, y_train)

theBestResult = gridSearchResult.best_score_
theBestParameters = gridSearchResult.best_params_

print(theBestResult)
print(theBestParameters)












































