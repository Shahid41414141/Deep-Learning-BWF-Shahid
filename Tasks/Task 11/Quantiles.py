import numpy as np

# Generate some data
data = np.random.normal(0, 1, 100)
data2 = 101

# Calculate the 25th, 50th (median), and 75th percentiles
q1 = np.percentile(data2, 25)
q2 = np.percentile(data2, 50)
q3 = np.percentile(data2, 75)

print("25th percentile:", q1)
print("Median:", q2)
print("75th percentile:", q3)
