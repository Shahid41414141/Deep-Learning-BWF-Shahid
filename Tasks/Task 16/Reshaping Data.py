import pandas as pd

# Create a dataframe
df = pd.DataFrame({'foo': ['one', 'one', 'two', 'two'],
                   'bar': ['A', 'B', 'C', 'D'],
                   'baz': [1, 2, 3, 4]})

# Reshape the dataframe
stacked = df.set_index(['foo', 'bar']).stack()
unstacked = stacked.unstack()

print(stacked)
print(unstacked)
