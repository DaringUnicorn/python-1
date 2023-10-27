"""
    to check the datatype of any dataset we can print the information about the dataset
which is df.info()

    to convert a column's data type :
df["C"] = df["C"].astype("float)

tasks:
Take a look at the .head() of the hits column.
Convert the hits column to type int.
Take a look at the .dtypes of the dataset again, and notice that the column type has changed.



answers:
# Print the head of the hits column
print(volunteer["hits"].head())

# Convert the hits column to type int
volunteer["hits"] = volunteer["hits"].astype("int")

# Look at the dtypes of the dataset
print(volunteer.dtypes)

"""



import pandas as pd

df = pd.read_csv("dataTypes.csv")

print("information about the table : \n", df.info())

print("*********************************************")

 
df["C"] = df["C"].astype("float") #converted the c colunm
print(df.dtypes)
print("converted C column to float : \n", df["C"])