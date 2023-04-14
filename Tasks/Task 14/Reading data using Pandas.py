import pandas as pd
import os
print(os.getcwd())


# read in the data file as a DataFrame
df = pd.read_csv('Final Result.csv')

print(df.head())
print(df.shape)
print(df.columns)
selected_columns = df[['State', 'TotalPop']]
print(selected_columns.head())


