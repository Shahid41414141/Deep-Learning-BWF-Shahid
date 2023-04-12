import numpy as np
# Create a 1D array of numbers from 0 to 9
a = np.arange(10)
print(a)
# Create a 3×3 numpy array of all True’s
b = np.arange(2,17,2, dtype=int).reshape(2,-1)
print(b)
# # Extract all odd numbers from array a
c = a[a%2==1]
print(c)
# # # Replace all odd numbers in array a with -1
a[a%2==1] = -1
print(a)
# # # Convert a 1D array to a 2D array with 2 rows
d = np.arange(10).reshape(2, -1)
print(d)


