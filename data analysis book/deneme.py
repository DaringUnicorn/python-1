import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Value': [10, 20, 15, 25, 30]
}

df = pd.DataFrame(data)
grouped = df.groupby('Category')

print(df)

for name, group in grouped:
    print("Group Name:", name)
    print(group)
    print("\n")
