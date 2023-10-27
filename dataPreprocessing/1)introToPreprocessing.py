""" 
    to find the information about the dataset let's say out dataset variable name is 
hiking and the information about the set can be shown in the console with hiking.info()

and also we can display the mean, standard deviation and quartiles through the 
hiking.describe()


    the first step to preprocess the data is removing the missing data :

        df for variable name for the dataframe
    
        1)df.dropna() method drops all rows which contains NaN values

        2)df.drop([indexes]) (ex: df.drop([1,2,3]) this means drop the first,
        second and third rows)

        3)df.drop("columnName", axis=1) the axis must be 1 in here to be able to drop 
    the column. So, axis = 0 means the horizontal and drops the row, and axis = 1 
    means the vertical and drops the column.

        4)df.isna() method returns the True/False values for each cell in the dataset
    and with that we can calculate the sum of the missing values in each column like this :
    df.isna().sum() in 

        5)if want to drop only the specified column's row for example in this case there
    is one missing value in the B column, and to drop that column we can write this:
    df.dropna(subset = ["B"])

        6)if we want to specify the number of missing values for example there are rows 
    which contains 3 or more missing values but we only want to display the rows with 3
    missing values. So, to be able to that df.dropna(thresh = 2)  2 means here bring
    the rows which contains at least 2 values

    tasks:
    Drop the Latitude and Longitude columns from volunteer, storing as volunteer_cols.
Subset volunteer_cols by dropping rows containing missing values in the category_desc, and store in a new variable called volunteer_subset.
Take a look at the .shape attribute of volunteer_subset, to verify it worked correctly.

    answers:
    # Drop the Latitude and Longitude columns from volunteer
volunteer_cols = volunteer.drop(["Latitude", "Longitude"], axis=1)
print(volunteer_cols)
# Drop rows with missing category_desc values from volunteer_cols
volunteer_subset = volunteer_cols.dropna(subset=["category_desc"])
print(volunteer_subset)
# Print out the shape of the subset
print(volunteer_subset.shape)


"""

import pandas as pd

df = pd.read_csv("sample.csv")

print(df.info())
print(df.describe())

print("************************************")

droppedMissingValues = df.dropna()
print("all missing values dropped : \n",droppedMissingValues)

print("************************************")

dropSelectedRows = df.drop([1,2,3])
print("selected rows dropped : \n", dropSelectedRows)

print("************************************")

dropColumnWithName = df.drop("A", axis=1)
print("the column with the given name dropped : \n", dropColumnWithName)

print("************************************")

missingValuesForEachCell = df.isna()
print("the missing values for each cell : \n", missingValuesForEachCell)

print("************************************")

numberOfMissingValues = df.isna().sum()
print("the number of missing values : \n", numberOfMissingValues)

print("************************************")

theSpecifiedColumnDrop = df.dropna(subset=["B"])
print("specified column's rows containing missing values dropped : \n", theSpecifiedColumnDrop)

print("************************************")

bringTheRowsWithGivenThresh = df.dropna(thresh=2)
print("brings the rows with at least two value contained : \n", bringTheRowsWithGivenThresh)

print("************************************")

