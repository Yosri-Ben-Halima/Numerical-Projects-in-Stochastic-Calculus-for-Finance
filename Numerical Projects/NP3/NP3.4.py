import numpy as np
import matplotlib.pyplot as plt

# Step 
dt = 0.01
# Number of paths
M = 100
# Time in years
T = 1
# Length
n = int(T/dt)
# Initial value
B0 = np.random.normal(0,np.sqrt(dt),M)
# Constructing covariance matrix 
i, j = np.indices((n+1,n+1))
C = 0.5*np.exp(-2*(np.maximum(i,j)-np.minimum(i,j))/(T/dt))
# Cholesky decomposition C = A*A'
A = np.linalg.cholesky(C)
# Sampling function
def SDG_Samples(N):
    global dt
    return np.random.normal(0,np.sqrt(dt),N)
# Generate the Brownian motion paths
paths = np.zeros((M, n+1))
for i in range(M):
    dW = SDG_Samples(n+1)
    y = np.dot(A, dW) 
    paths[i] = B0[i] + y

# Compute proportion of time spent in positive half-plane
pos_time = np.sum(paths > 0, axis=0) * dt
X = pos_time / T

# Plot histogram
plt.hist(X, bins=50, density=True, color='blue', alpha=0.5)

# Overlay arcsine density function
x = np.linspace(0+dt, 1-dt, 100) # +/- dt: to avoid ZeroDivisionError
y = 1 / (np.pi * np.sqrt(x * (1-x)))
plt.plot(x, y, color='red')

plt.title("Histogram of X $(X_t >0)$ and Arcsine Density Function")
plt.xlabel("Proportion of Time Spent Positive")
plt.ylabel("Density")

plt.show()