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
# Hurst indexes 
H = [0.1,0.5,0.9]
# Initial value
B0 = 0
# Sampling function
def SDG_Samples(N):
    global dt
    return np.random.normal(0,np.sqrt(dt),N)
# Simulating paths for each H 
P = {}
# Plot 
fig, axes = plt.subplots(1, len(H), figsize=(1.5*10, 1.5*3))
for h in H:
    # Constructing covariance matrix & Cholesky decomp
    C = np.zeros((n,n))
    for i in range(1,1+n):
        for j in range(1,1+n):
            C[i-1,j-1] = ((j/n)**(2*h)-np.abs((i-j)/n)**(2*h)+(i/n)**(2*h))/2
    print(C)
    # Cholesky decomposition C = A*A'
    A = np.linalg.cholesky(C)
    # Generate the Brownian motion paths
    paths = np.zeros((M, n+1))
    for i in range(M):
        dW = SDG_Samples(n)
        y = np.dot(A, dW)
        y = np.insert(y, 0, 0)
        paths[i] = B0 + y
    P[h] = paths
# Plot the Brownian motion paths
t = np.arange(0, T+dt, dt)
for j,h in enumerate(H):
    axes[j].grid(True)
    axes[j].set_xlabel("Time")
    axes[j].set_ylabel("Value")
    for i in range(M):
        axes[j].plot(t, P[h][i])   
    axes[j].set_title(f"H = {h}")
    
plt.show()    
