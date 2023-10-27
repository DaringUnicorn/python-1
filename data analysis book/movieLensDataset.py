import pandas as pd

userNames = ["userId", "gender", "age", "occupation", "zip"]
# kolon isimleri yazdık sonrasında onları users.dat dosyasoyla eşleştirdik
users = pd.read_table(r"C:/Users/Ayhan/Desktop/book/users.dat", sep="::", header=None, names=userNames)

# print(users)

ratingNames = ["userId", "movieId", "rating", "timestamp"]
# user için yaptığımızı burada da yaptık aynı şekilde

ratings = pd.read_table(r"C:/Users/Ayhan/Desktop/book/ratings.dat", sep="::", header=None, names=ratingNames)

# print(ratings)

movieNames = ["movieId", "title", "genres"]
movies = pd.read_table(r"C:/Users/Ayhan/Desktop/book/movies.dat", sep="::", header=None, names= movieNames, encoding='latin-1')

# print(movies)


data = pd.merge(pd.merge(ratings, users),movies)
"""
    pd.merge() fonksiyonu buradaki örnek için ratings ve users tablolarını birleştiriyor. Nasıl mı?

    ratings tablosundaki userId kısmıyla users tablosundaki userId kısımlarını birbirleriyle ilişkilendirip
gerekli userId kolonuna users tablosundan aldığı user bilgilerini yazıyor. o7

"""



print(data.iloc[0])


meanRatings = data.pivot_table("rating", "title", columns="gender", aggfunc="mean")

# data içerisinde bulunan genderı kolon olarak title ı row olarak alıp ratinglerin de meanini alıyor
print(meanRatings)

groupData = data.groupby("title").size()

activeTitles = groupData.index[groupData >= 250]

print(activeTitles)


# meanRatings.iloc[activeTitles]

# print(meanRatings.sort_values(by="F",ascending=False))

meanRatings["difference"] = meanRatings["M"] - meanRatings["F"]
print(meanRatings.sort_values(by= "difference", ascending=False))

print(data.groupby("title")["rating"].std())