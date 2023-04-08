import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
# Step 
dt = 0.01
# Number of paths
M = 1
# Time in years
T = 1
# Length
n = int(T/dt)
# Initial value
B0 = 0
# Constructing covariance matrix 
C = np.zeros((n-1,n-1))
for i in range(1,n):
    for j in range(1,n):
        C[i-1,j-1] = (min(i,j)/n)*(1-(max(i,j)/n))
# Cholesky decomposition C = A*A'
A = np.linalg.cholesky(C)
# Sampling function
def SDG_Samples(N):
    global dt
    return np.random.normal(0,np.sqrt(dt),N)
# Generate the Brownian motion paths
paths = np.zeros((M, n+1))
for i in range(M):
    dW = SDG_Samples(n-1)
    y = np.dot(A, dW)
    y = np.insert(y, 0, 0)
    y = np.append(y, 0)
    paths[i] = B0 + y
np.random.seed(42)
# Constructing covariance matrix 
C1 = np.zeros((100,100))
for i in range(100):
    for j in range(100):
        C1[i,j] = (1 + min(i,j)) / 100
# Cholesky decomposition C = A*A'
A1 = np.linalg.cholesky(C1)
z1 = SDG_Samples(n)
y1 = np.dot(A1, z1)
y1 = np.insert(y1,0,B0)
Bt = y1 - y1[-1]*np.arange(0, T+dt, dt)
# Plot the Brownian motion paths
t = np.arange(0, T+dt, dt)
for i in range(M):
    plt.plot(t, paths[i], label="Cholesky")
plt.plot(t,Bt,label="Not Cholesky")
plt.grid(True)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('100 Paths of Brownian Motion')
plt.show()



