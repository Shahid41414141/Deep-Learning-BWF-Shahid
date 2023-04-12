import pandas as pd

# read in the data file as a DataFrame
df = pd.read_csv('1.merged.csv')

# split the GenderPop column into Men and Women columns
df[['Men', 'Women']] = df['GenderPop'].str.split('_', expand=True)

# remove the 'M' and 'F' characters from the Men and Women columns
df['Men'] = df['Men'].str.replace('M', '').astype(int)
df['Women'] = df['Women'].str.replace('F', '').replace('', '0').astype(int)

# fill in values in Women column with GenderPop-Men values
df['Women'] = df['TotalPop'] - df['Men']


# Drop the GenderPop column
df = df.drop(columns=['GenderPop'])

print(df.columns)


# Drop the "Unnamed" column
df = df.drop(columns=['Unnamed: 0'])

# print the resulting DataFrame to the console
print(df.head())

# write the resulting DataFrame to a new CSV file
df.to_csv('2.After_split.csv', index=False)

