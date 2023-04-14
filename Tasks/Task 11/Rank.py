import numpy as np

# Generate some data
data = np.array([5, 2, 7, 1, 9])

# Calculate the rank of the data
rank = np.argsort(data)
print("Rank:", rank)

# Sort the data in ascending order
data_sorted = np.sort(data)
print("Sorted data:", data_sorted)
