import numpy as np

# Create two arrays with different shapes
a = np.array([1, 2, 3])
b = np.array([[4], [5], [6]])

# Print the shapes of the arrays
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)

# Perform arithmetic operations using broadcasting
c = a + b
d = a * b

# Print the result arrays and their shapes
print("Result of a + b:", c)
print("Shape of c:", c.shape)
print("Result of a * b:", d)
print("Shape of d:", d.shape)
