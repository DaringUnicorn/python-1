import pandas as pd

path = r"C:/Users/Ayhan/Downloads/names/yob1880.txt"

names1880 = pd.read_csv(path, names=["name", "gender", "births"])

# print(names1880)

data1 = names1880.groupby("gender")
# for i,j in data1:
    
#     print(i)
#     print("\n")
#     print(j)

femaleData = data1.get_group("F")
print("female data : \n", femaleData)
maleData = data1.get_group("M")
print("male data : \n", maleData)

print("female births : ",femaleData["births"].sum())
print("male births : ",maleData["births"].sum())

# below codes have the same function with the above codes

print(names1880.groupby("gender").births.sum())


# names dosyasındaki bütün dosyaları tek bir dataframede birleştiriyoruz.
years = range(1880, 2023)

pieces = []
columns = ["name", "gender", "births"]

for year in years:

    path = r"C:/Users/Ayhan/Downloads/names/yob%d.txt" %year
    frame = pd.read_csv(path, names=columns)

    frame["year"] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)

totalBirths = names.pivot_table("births", "year", columns="gender", aggfunc=sum)