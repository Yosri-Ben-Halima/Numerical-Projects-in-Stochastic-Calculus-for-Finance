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
# Type of Ornstein-Uhlenbeck process: 0 for stationary, 1 for non-stationary
Type = int(input("Type 0 for stationary or 1 for non-stationary: "))
# Initial value
if Type == 1 :
    B0 = [0]*M
else:
    B0 = np.random.normal(0,np.sqrt(dt),M)
# Constructing covariance matrix 
if Type == 1:
    i, j = np.indices((n,n))
    C = 0.5*np.exp(-2*(np.maximum(i,j)-np.minimum(i,j))/(T/dt))*(1-np.exp(-2*(np.minimum(i,j)+1)/(T/dt)))
else:
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
    dW = SDG_Samples(n+1-Type)
    y = np.dot(A, dW)
    if Type == 1:
        y = np.insert(y, 0, 0) 
    paths[i] = B0[i] + y
# Plot the Brownian motion paths
t = np.arange(0, T+dt, dt)
for i in range(M):
    plt.plot(t, paths[i])
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('100 Paths of Brownian Motion')
plt.show()

