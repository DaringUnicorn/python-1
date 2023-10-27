import pandas as pd

df = pd.read_csv("thresh.csv")

cols = df.drop(["Latitude", "Longitude"], axis=1)

print(cols)

print(cols.dropna())