import numpy as np
import matplotlib.pyplot as plt

# Step 
dt = 0.01
# Number of paths
M = 100
# Time in years
T = 1
# Initial value
B0 = 0
# Constructing covariance matrix 
C = np.zeros((100,100))
for i in range(100):
    for j in range(100):
        C[i,j] = (1 + min(i,j)) / 100
# Cholesky decomposition C = A*A'
A = np.linalg.cholesky(C)
# Sampling function
def SDG_Samples(N):
    return np.random.standard_normal(N)
# Generate the Brownian motion paths
paths = np.zeros((M, 101))
for i in range(M):
    z = np.random.normal(size=100)
    y = np.dot(A, z)
    paths[i,1:101] = (y)
    paths[i,0] = B0
# Plot the Brownian motion paths
t = np.arange(0, 1.01, 0.01)
for i in range(M):
    plt.plot(t, paths[i])
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('100 Paths of Brownian Motion')
plt.show()


