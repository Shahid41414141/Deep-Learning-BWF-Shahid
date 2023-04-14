import numpy as np
import matplotlib.pyplot as plt

# Generate some data
data = np.random.normal(0, 1, 10000)

# Plot the histogram
plt.hist(data, bins=50, density=True)

# Plot the normal distribution
mu, sigma = 0, 1
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2)))

plt.show()
