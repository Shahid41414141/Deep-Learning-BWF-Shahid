import numpy as np

# Create two random 2D arrays with the same shape
arr1 = np.random.randint(0, 10, size=(2, 3))
arr2 = np.random.randint(0, 10, size=(2, 3))

# Add the two arrays
arr_sum = arr1 + arr2

# Subtract the second array from the first
arr_diff = arr1 - arr2

# Multiply the two arrays element-wise
arr_prod = arr1 * arr2

# Divide the first array by the second element-wise
arr_div = arr1 / arr2

# Print the results
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)
print("Array Sum:\n", arr_sum)
print("Array Difference:\n", arr_diff)
print("Array Product:\n", arr_prod)
print("Array Division:\n", arr_div)
