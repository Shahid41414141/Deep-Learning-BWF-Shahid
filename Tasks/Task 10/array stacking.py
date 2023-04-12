import numpy as np
# #Vstack of 1D arrays
a = np.arange(10).reshape(1, -1)
print(a)

b = np.arange(20, 30, dtype=int).reshape(1, -1)
print(b)

e = np.vstack([a, b])
print(e)

#Vstack of 2D arrays
a = np.arange(10).reshape(2, -1)
print(a)

b = np.arange(20, 30, dtype=int).reshape(2, -1)
print(b)

e = np.vstack([a, b])
print(e)

#Hstack of 1D arrays
a = np.arange(10).reshape(1, -1)
print(a)

b = np.arange(20, 30, dtype=int).reshape(1, -1)
print(b)

e = np.hstack([a, b])
print(e)

#Hstack of 2D arrays
a = np.arange(10).reshape(2, -1)
print(a)

b = np.arange(20, 30, dtype=int).reshape(2, -1)
print(b)

e = np.hstack([a, b])
print(e)

#stack of 1D arrays
a = np.arange(10).reshape(1, -1)
print(a)

b = np.arange(20, 30, dtype=int).reshape(1, -1)
print(b)

e = np.stack([a, b])
print(e)

#stack of 2D arrays
a = np.arange(10).reshape(2, -1)
print(a)

b = np.arange(20, 30, dtype=int).reshape(2, -1)
print(b)

e = np.stack([a, b])
print(e)





