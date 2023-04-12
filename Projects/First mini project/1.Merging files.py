import os
import pandas as pd

# set the directory path containing the CSV files
dir_path = 'D:\Bytewise\Projects\First mini project\Data'

# initialize an empty list to store the DataFrames
dfs = []

# loop through all CSV files in the directory
for file in os.listdir(dir_path):
    if file.endswith('.csv') and file.startswith('states'):
        # read in the CSV file as a DataFrame
        df = pd.read_csv(os.path.join(dir_path, file))
        
        # append the DataFrame to the list of DataFrames
        dfs.append(df)

# concatenate all DataFrames in the list into a single DataFrame
combined_df = pd.concat(dfs)

# write the combined DataFrame to a new CSV file
combined_df.to_csv('1.merged.csv', index=False)
