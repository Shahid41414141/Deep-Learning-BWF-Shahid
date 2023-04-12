import pandas as pd

# load the csv file into a pandas DataFrame
df = pd.read_csv('3.After duplicates.csv')

# select the columns of interest
cols = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']
cols1 = ['Income']

# remove the signs from the selected columns
df[cols]= df[cols].apply(lambda x: x.str.rstrip('%'))
df[cols1] = df[cols1].apply(lambda x: x.str.replace('$', '',regex=False).str.strip())

# convert the selected columns to float
df[cols] = df[cols].astype('float')
df[cols1] = df[cols1].astype('float')

# remove the NaN values from the selected columns
df[cols] = df[cols].fillna(0)

# save the updated DataFrame to a new csv file
df.to_csv('Final Result.csv', index=False)
