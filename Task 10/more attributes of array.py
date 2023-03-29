import numpy as np

# Create a 2D array with shape (3, 4)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Calculate the sum of all elements in the array
total_sum = np.sum(arr)

# Calculate the sum of each column in the array
col_sum = np.sum(arr, axis=0)

# Calculate the sum of each row in the array
row_sum = np.sum(arr, axis=1)

# Transpose the array
arr_transpose = np.transpose(arr)

# Calculate the dot product of the array with itself
arr_dot = np.dot(arr, arr_transpose)

# Print the results
print("Array:\n", arr)
print("Total Sum:", total_sum)
print("Column Sum:", col_sum)
print("Row Sum:", row_sum)
print("Array Transpose:\n", arr_transpose)
print("Array Dot Product:\n", arr_dot)
