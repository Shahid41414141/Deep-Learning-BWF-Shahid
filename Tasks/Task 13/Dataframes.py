import pandas as pd

# create a dictionary
my_dict = {'name': ['John', 'Jane', 'Bob', 'Mary'],
           'age': [25, 30, 40, 50],
           'gender': ['M', 'F', 'M', 'F']}

# create a DataFrame from the dictionary
my_df = pd.DataFrame(my_dict)

# print the DataFrame
print(my_df)
