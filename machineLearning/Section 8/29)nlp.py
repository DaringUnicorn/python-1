import numpy as np
import pandas as pd
import re
import nltk


from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_decomposition import confusion_matrix


data = pd.read_csv("restaurantReviews.csv")
review = re.sub('[^a-zA-Z]',' ',data["Review"][0])


porterStemmer = PorterStemmer()

nltk.download('stopwords')

#Preprocessing 
derlem = []

for i in range(1000):
    
    review = review.lower()
    review = review.split()
    review = [porterStemmer.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    derlem.append(review)
    
#Feature Extraction (Öznitelik Çıkarımı)
#Bag of Words BOW
countVectorizer = CountVectorizer(max_features=1000)

X = countVectorizer.fit_transform(derlem).toarray()  #bağımsız değişken
Y = review.iloc[:,1].values #bağımlı değişken


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size= 0.20, random_state=0)
    
gaussianNaiveBayes = GaussianNB()
gaussianNaiveBayes.fit(x_train,y_train)

y_prediction = gaussianNaiveBayes.predict(x_test)


confusionMatrix = confusion_matrix(y_test, y_prediction)

print(confusionMatrix)













