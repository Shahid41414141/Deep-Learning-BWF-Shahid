import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a pandas DataFrame
df = pd.read_csv('Final Result.csv')

# Select the columns that contain race data
race_cols = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']

# Create a histogram for each race category
for col in race_cols:
    plt.hist(df[col], bins=20)
    plt.title('Histogram of ' + col)
    plt.xlabel('Proportion of Population')
    plt.ylabel('Frequency')
    plt.show()
