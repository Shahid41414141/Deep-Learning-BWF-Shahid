import numpy as np
from scipy import stats

# Mean
data = np.array([1, 2, 3, 4, 5, 6, 7])
mean = np.mean(data)
print("Mean:", mean)

# Median
data = np.array([1, 2, 3, 4, 5, 11, 12, 13, 14, 15])
median = np.median(data)
print("Median:", median)

# Mode
data = np.array([1, 2, 3, 3, 4, 4, 4, 5, 5])
mode = stats.mode(data, keepdims=True)
print("Mode:", mode.mode[0])

# Range
data = np.array([1, 2, 3, 4, 5, 55])
range = np.ptp(data)
print("Range:", range)
