import pandas as pd
import numpy as np
""" 
    pandas serileri bir key sütunu ya da indeks sütunu bir de onlara karşılık gelen bir 
value sütunundan oluşuyordu. pandas dataframeleri ise pandas serilerinin birbirine eklenmesiyle
oluşturulan yapılardır.

 """

serie1 = pd.Series([3,2,0,1])
serie2 = pd.Series([0,3,7,2])


# oluşturduğumuz iki seriyi birleştirmek için sütun adı ve yanına seriyi yazıyoruz

data = dict(apples = serie1, oranges = serie2)

df = pd.DataFrame(data=data)

print(f"dataframe : \n{df}")


dataframe = pd.DataFrame()

print(f"boş dataframe : \n{dataframe}")


dataframe = pd.DataFrame([1,2,3,4])

print(f" dataframe : \n{dataframe}")


dataframe = pd.DataFrame([["Ahmet", 50],["Ali",60],["Yağmur", 70],["Çınar",80]])

print(f" dataframe : \n{dataframe}")


data = [["Ahmet", 50],["Ali",60],["Yağmur", 70],["Çınar",80]]

dataframe = pd.DataFrame(data=data, columns=["Name", "Grade"], index=[1,2,3,4])

print(f" dataframe : \n{dataframe}")


# dictionary ile dataframe oluşturma

dict = {"Name": ["Ahmet", "Ali", "Yağmur", "Çınar"],
        "Grade": [50,60,70,80]}

dataframe = pd.DataFrame(dict)

print(f" dictionary ile dataframe : \n{dataframe}")


dataframe = pd.DataFrame(dict, index=["212","232","236","456"])

print(f"indeks ataması yapılan dictionary ile dataframe : \n{dataframe}")

