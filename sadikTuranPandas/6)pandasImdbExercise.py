import pandas as pd
import numpy as np

# 1- Dosyada hakkındaki bilgiler.
df = pd.read_csv("imdb.csv")
print(df)

# 2- ilk 5 kaydı gösterin

print(df.head())
# 3- ilk 10 kaydı gösterin
print(df.head(10))


# 4- Son 5 kaydı gösterin
print(df.tail())

# 5- Son 10 kaydı gösterin
print(df.tail(10))


# 6- Sadece Movie Title kolonunu alın.

print(df["Movie_Title"])


# 7- Sadece Movie_Tit1e kollonunu içeren ilk 5 kaydı alın.
print(df["Movie_Title"].head())


# 8- Sadece Movie T itle ve Rating kolonunu içeren ilk 5 kaydı alın.
print(df[["Movie_Title","Rating"]].head())


# 9- Sadece Movie T itle ve Rating kolonunu içeren son 7 kaydı alın.
print(df[["Movie_Title","Rating"]].tail(7))


# 10- Sadece Movie T itle ve Rating kolonunu içeren ikinci 5 kaydı alın.
print(df.loc[5:10,["Movie_Title","Rating"]])


# 11- Sadece Movie T itle ve Rating kolonunu içeren ve imdb puanı 8.0
# ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
print(df[df["Rating"] >= 8.0][["Movie_Title", "Rating"]])

# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.

print(df[(2014 <= df["YR_Released"]) & (2015 >= df["YR_Released"])][["Movie_Title", "Rating"]])

# 13- DeğerIendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı
# 8 ile 9 arasında olan filmleri listeleyiniz.

print(df[(df["Num_Reviews"] > 100000) | ((df["Rating"] <= 9.0) & (df["Rating"] >= 8.0))][["Movie_Title", "Rating","Num_Reviews"]])
