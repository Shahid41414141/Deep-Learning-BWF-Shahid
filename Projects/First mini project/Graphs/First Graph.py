import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a pandas DataFrame
df = pd.read_csv('Final Result.csv')

# Select the 'State', 'Income', and 'Women' columns
df = df[['State', 'Income', 'Women', 'TotalPop']]

# Calculate the proportion of women in each state
prop_women = df['Women'] / df['TotalPop']

# Create a scatterplot
plt.scatter(prop_women, df['Income'])
plt.xlabel('Proportion of Women in State')
plt.ylabel('Income in State')
plt.title('Scatterplot of Income vs Proportion of Women by State')
plt.show()
