# Handling Missing Data
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8], 'C': [9, 10, 11, 12]})
print(df)

# Check for missing values
print(df.isnull())

# Drop rows with missing values
print(df.dropna())

# Drop columns with missing values
print(df.dropna(axis=1))

# Fill missing values with 0
print(df.fillna(0))

# Fill missing values with the mean of the column
print(df.fillna(df.mean()))

# Fill missing values with the mode of the column
print(df.fillna(df.mode().iloc[0]))
