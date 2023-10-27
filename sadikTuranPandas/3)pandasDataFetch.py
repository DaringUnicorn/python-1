import pandas as pd
import numpy as np

df = pd.read_csv("sample.csv")

print("csv dosyası : \n",df)


df = pd.read_json("sample.json", encoding="UTF-8")

print("json dosyası : \n",df)

df = pd.read_excel("sample.xlsx")

print("excel dosyası : \n",df)
