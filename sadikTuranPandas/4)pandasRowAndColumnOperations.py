import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(3,3), index=["A","B","C"], columns=["Column1", "Column2", "Column3"])

result = df

print("dataframe : \n", result)

print("column1 data type : \n", type(result["Column1"]))


# birden fazla sütun seçimi yaparken bu seçimleri bir liste içerisinde belirtmemiz gerekir 
print(f"birden fazla kolon seçimi : \n{result[["Column1", "Column2"]]}")

""" 
    satıra göre seçme işlemini yapmak için aşağıdaki satırdaki gibi bi kod yazmamız gerek
ve bu kod da bize verilen satırdaki sütunları bir seri olarak döndürür.

    metodun tam kullanımı:
.loc["row","column"] 
sadece row seçimi için => .loc["row"]

sütun seçimi için => .loc[":", "column"]

 """
print(f"loc metodu ve kullanımı : \n{result.loc["A"]}")
print(f"loc metodu veri tipi : \n{type(result.loc["A"])}")
print(f"loc metodu satıların tümü ve seçili kolon çağırılması : \n{result.loc[:,"Column1"]}")
print(f"loc metodu satıların tümü ve seçili kolon çağırılması : \n{result.loc[:,["Column1", "Column2"]]}")

# belli bir aralıktaki kolonların seçilmesi için 

print(f"loc metodu ile kolon aralığı vererek çağırma : \n{result.loc[:,"Column1":"Column3"]}")


print(f"loc metodu ile satır ve sütun aralığı vererek çağırma : \n{result.loc["A":"C",:"Column3"]}")


print(f"loc metodu ile spesifik satır ve sütundaki değeri alma : \n{result.loc["A","Column2"]}")


# dataframe e yeni bir column ekleme

df["Column4"] = pd.Series(np.random.randn(3),["A","B","C"])

print(f"yeni sütun eklenmiş dataframe : \n{df}")

# yeni bir column ekleme fakat frame içerisinde var olan iki column toplamının yeni columna eşitlenmesi

df["Column5"] = df["Column1"] + df["Column3"]

print(f"birinci ve üçüncü columnların yeni bir column olarak eklenmiş hali : \n{df}")

# column silmek


print(f"beşinci columnun silinmiş hali : \n{df.drop("Column5",axis=1)}")
