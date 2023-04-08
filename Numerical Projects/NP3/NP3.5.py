import numpy as np
import matplotlib.pyplot as plt

# n = 1,2,...,20
n = 20
# Step 
dt = 2**(-n)
# Number of paths
M = 1
# Time in years
T = 1
# Number of steps
N = int(T/dt)
# Initial value
B0 = 0
# Containers 
V = []
QV = []
# Create a matrix to store Brownian motion paths with M number of paths and n timesteps
B = np.zeros(N+1)
# Generate random increments using normal distribution with mean 0 and standard deviation sqrt(dt) for each timestep
I = np.random.normal(0,np.sqrt(dt),N)
# Insert B0 as the initial condition to the increment array
I = np.insert(I, 0, B0)
# Calculate cumulative sum of the increments to get the Brownian motion path
B = np.cumsum(I)
for i in range(1,n+1):
    v,qv = 0,0
    for j in range(2**i):
        v += abs(B[(j+1)*(2**(n-i))]-B[(j)*(2**(n-i))])
        qv += (B[(j+1)*(2**(n-i))]-B[(j)*(2**(n-i))])**2
    V.append(v)
    QV.append(qv)

L = [i for i in range(1,n+1)]

# Plot V and QV in subplots
fig, axs = plt.subplots(2, sharex=True)
axs[0].plot(L,V,label='Variation(n)')
axs[0].set_ylabel('Variation')
axs[0].legend()
axs[0].grid(True)
axs[1].plot(L,QV,label='Quadratic Variation(n)')
axs[1].set_xlabel('n')
axs[1].set_ylabel('Quadratic Variation')
axs[1].grid(True)
axs[1].legend()
plt.show()
