import pandas as pd

# read the csv file
df = pd.read_csv('2.After_split.csv')

df.drop_duplicates(keep='first', inplace=True)

df.to_csv('3.After duplicates.csv', index=False)

