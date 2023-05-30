import numpy as np
import matplotlib.pyplot as plt

def levy_brownian(N):
    # Generate N steps for Brownian motion
    b = np.random.normal(0, 1, N)
    # Generate N-1 steps for Lévy process
    z = np.random.normal(0, 1, N-1)
    # Calculate the increments for the Lévy process
    inc = np.zeros(N)
    inc[1:] = np.exp(z/2) * np.sin(np.cumsum(np.sqrt(2/N)*np.pi*z))
    # Combine the Brownian motion and Lévy process increments
    return np.cumsum(b + inc)

# Generate 10 paths of standard Brownian motion for N=5, N=20, and N=100
N_values = [5, 20, 100]
num_paths = 10

fig,axe = plt.subplots(1, 3)
for j,N in enumerate(N_values):
    for i in range(num_paths):
        path = levy_brownian(N)
        axe[j].plot(path)
    axe[j].set_title(f'Standard Brownian Motion with N={N}')
plt.show()    