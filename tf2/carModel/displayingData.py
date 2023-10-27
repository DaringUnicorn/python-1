import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


dataframe = pd.read_excel("merc.xlsx")

print(dataframe.head(10))


print(dataframe.describe())


# null veri kontrolü 


print(dataframe.isnull().sum())

