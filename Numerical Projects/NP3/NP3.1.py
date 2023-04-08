import numpy as np
import matplotlib.pyplot as plt

# Step 
dt = 0.01
# Number of paths
M = 100
# Time in years
T = 1
# Number of steps
n = int(T/dt)
# Initial value
B0 = 0

# Create a matrix to store Brownian motion paths with M number of paths and n timesteps
Paths = np.zeros((M, n))

# Generate M number of paths for Brownian Motion
for i in range(M):
    # Generate random increments using normal distribution with mean 0 and standard deviation sqrt(dt) for each timestep
    I = np.random.normal(0,np.sqrt(dt),n-1)
    
    # Insert B0 as the initial condition to the increment array
    I = np.insert(I, 0, B0)
    
    # Calculate cumulative sum of the increments to get the Brownian motion path
    Paths[i] = np.cumsum(I)

# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(8,5))
# Plot Brownian motion paths on the first subplot
t = np.arange(0, T, dt)
for i in range(M):
    ax.plot(t, Paths[i])
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('100 Paths of Brownian Motion')

# Display the final plot
plt.show()   
