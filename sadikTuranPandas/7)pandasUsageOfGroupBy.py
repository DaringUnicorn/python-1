import pandas as pd
import numpy as np

personeller = {
'Çalışan':[ 'Ahmet Yılmaz' , 'Can Ertürk' , 'Hasan Korkmaz' , 'Cenk Saymaz' , 'Ali Turan', "Rıza Ertürk", "Mustafa Can"],
'Departman':[ 'İnsan Kaynakları' , 'Bilgi İşlem' , 'Muhasebe', 'İnsan Kaynakları',"Bilgi İşlem", "Muhasebe", "Bilgi İşlem"],
'Yaş': [30,25,45,50,23,34,42],
'Semt':[ 'Kadıköy' , 'Tuzla' , 'Maltepe' , 'Tuzla', 'Maltepe' , 'Tuzla' , 'Kadıköy' ],
'Maaş':[5000, 3000, 4000, 3500, 2750, 6500,4500]
}

df = pd.DataFrame(personeller)

print("maaş toplam : ",df["Maaş"].sum())



# gruplama işlemi


print(f"departman sütununa göre gruplanmış dataframe : \n{df.groupby("Departman").groups}")

print(f"departman ve semt sütununa göre gruplanmış dataframe : \n{df.groupby(["Departman","Semt"]).groups}")

semtler = df.groupby("Semt")

for name, group in semtler:
    print(name)
    print(group)

for name, group in df.groupby("Departman"):
    print(name)
    print(group)

# grubun içindeki gruba erişmek

print(f"grubun içindeki grup : \n{df.groupby("Semt").get_group("Kadıköy")}")

print(f"grubun içindeki grup : \n{df.groupby("Departman").get_group("Muhasebe")}")

# verilen sütundaki verilerin toplamı

print(f"sütun toplamı : \n{df.groupby("Departman").sum()}")

print(f"sütun ortalaması : \n{df.groupby("Departman")[["Maaş", "Yaş"]].mean()}")

# sütundaki veri sayısı

print(f"veri sayısı : \n{df.groupby("Semt")["Çalışan"].count()}")

print(f"en büyük veriyi getirme : \n{df.groupby("Departman")["Yaş"].max()}")

print(f"en küçük veriyi getirme : \n{df.groupby("Departman")["Maaş"].min()}")


print(f"muhasebe departmanındaki en düşük maaşlı kimseyi getirir : \n{df.groupby("Departman")["Maaş"].min()["Muhasebe"]}")


print(f"departmana göre ortalama alır : \n{df.groupby("Departman")[["Maaş", "Yaş"]].mean()}")