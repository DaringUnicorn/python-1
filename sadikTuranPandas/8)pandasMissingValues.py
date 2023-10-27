import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data=data, index=["a","c","e","f","h"], columns=["Column1","Column2","Column3"])

print(f"tertemiz teazecik dataframe : \n{df}")

# aşağıdaki satırda önceden tanımlanmış indeksleri yeniden tanımlayabiliyoruz


df = df.reindex(["a","b","c","d","e","f","g","h"])
print(f"reindex metoduyla tazelenmiş dataframe : \n{df}")

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]

df["Column4"] = newColumn


# sütun atma işlemi
print(f"verilen sütun ve axis=1 parametresiyle sütun komple silinir : \n{df.drop("Column1", axis=1)}")

# birden fazla sütun silme işlemi

print(f"liste halinde verilen sütunlar ve axis=1 parametresiyle sütunlar komple silinir : \n{df.drop(["Column1","Column3"], axis=1)}")


# satır silme işlemi

print(f"verilen satır ve axis=0 parametresiyle satır komple silinir : \n{df.drop("a", axis=0)}")

print(f"liste halinde verilen satırlar ve axis=0 parametresiyle satırlar komple silinir : \n{df.drop(["a","b","h"], axis=0)}")


# null değerleri veya NaN değerlerin tespiti

print(f"içerisinde NaN olan hücreler True değer içerenler ded False değer dönecektir : \n{df.isnull()}")

print(f"içerisinde NaN olan hücreler False değer içerenler ded True değer dönecektir : \n{df.isnull()}")

print(f"NaN değerlerin adedi : \n{df.isnull().sum()}")

print(f"istenilen columndaki NaN değerlerin adedi : \n{df["Column1"].isnull().sum()}")

print(f"NaN değerlerin bulunduğu hücrelerin getirilmesi : \n{df[df["Column1"].isnull()]}")

print(f"NaN değerlerin bulunduğu hücrelerin getirilmesi : \n{df[df["Column1"].isnull()]["Column1"]}")


print(f"NaN olmayan değerlerin bulunduğu hücrelerin getirilmesi : \n{df[df["Column1"].notnull()]}")

print(f"NaN olmayan değerlerin bulunduğu hücrelerin getirilmesi : \n{df[df["Column1"].notnull()]["Column2"]}")


# herhangi bir kolon ya da satır içerisinde bir NaN değer varsa o satır ya da sütunun komple silinmesi

print(f"içerisinde NaN değer bulunan satırların silinmesi : \n{df.dropna()}") 

#   dropna() fonksiyonunn how parametresinie any verildiğinde herhangi bir yerde bir tane bile
# NaN değer var olması durumunda default axis=0 olduğundan satır silinir. all dersek de 
# satırın tamamı null ise silnir.


print(f"dropna fonksiyonuna subset verilerek NaN değer aranması : \n{df.dropna(subset=["Column1", "Column2"], how="all")}")


print(f"dropna fonksiyonuna subset verilerek NaN değer aranması : \n{df.dropna(subset=["Column1", "Column2"], how="any")}")


#  dropna() fonksiyonunda thresh parametresi : bu parametreye verilen bir örneğin 3 şunu ifade eder:
# eğer verilen axiste 3 tane normal değer varsa o satırı ya da sütunu getir.

print(f"satırda en az 2 tane normal veri olanları getiren kod : \n{df.dropna(thresh=2,axis=0)}")

print(f"sütunda en az 5 tane normal veri olanları getiren kod : \n{df.dropna(thresh=5,axis=1)}")

# NaN hücreleri fillna() fonksiyonu ile dolduruyoruz

print(f"NaN değerleri 'no input' değeriyle dolduralım : \n{df.fillna("no input")}")