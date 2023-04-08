import numpy as np
import matplotlib.pyplot as plt

# Define parameters
n = 1000      # number of paths
T = 1         # total time
dt = 0.01     # time step

# Generate Brownian motion paths
t = np.linspace(0, T, int(T/dt)+1)
dB = np.sqrt(dt) * np.random.randn(len(t)-1, n)
B = np.cumsum(dB, axis=0)

# Compute proportion of time spent in positive half-plane
pos_time = np.sum(B > 0, axis=0) * dt
X = pos_time / T

# Plot histogram
plt.hist(X, bins=50, density=True, color='blue', alpha=0.5)

# Overlay arcsine density function
x = np.linspace(0+dt, 1-dt, 100) # +/- dt: to avoid ZeroDivisionError
y = 1 / (np.pi * np.sqrt(x * (1-x)))
plt.plot(x, y, color='red')

plt.title("Histogram of X $(B_t >0)$ and Arcsine Density Function")
plt.xlabel("Proportion of Time Spent Positive")
plt.ylabel("Density")

plt.show()

