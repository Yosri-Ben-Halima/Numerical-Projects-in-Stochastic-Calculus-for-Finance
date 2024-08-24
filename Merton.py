import numpy as np 
import matplotlib.pyplot as plt 

def simulate_jump_diffusion(S0, mu, sigma, T, M, dt, lambda_j, mu_j, sigma_j):
    """
    Simulates a path of the Merton jump diffusion model.

    Parameters:
    - S0: Initial asset price.
    - mu: Drift component.
    - sigma: Volatility of the continuous part.
    - T: Time to maturity.
    - M: Number of steps.
    - dt: Time increment.
    - lambda_j: Intensity of jumps.
    - mu_j: Mean of jump size.
    - sigma_j: Volatility of jump size.
    
    Returns:
    - A numpy array representing the asset price path.
    """
    S = np.zeros(M)
    S[0] = S0

    for t in range(1, M):
        Z = np.random.normal(0, 1)
        N = np.random.poisson(lambda_j * dt)
        J = np.random.normal(mu_j, sigma_j) if N > 0 else 0
        S[t] = S[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z + J)

    return S

np.random.seed(42)

# Parameters
S0 = 100
mu = 0.05
sigma = 0.2
T = 1.0 # 1 year
M = 252 # 252 trading days in a year
dt = T / M
lambda_j = 0.1
mu_j = 0.02
sigma_j = 0.1

# Simulate path
paths = []
for i in range(10):
    paths.append(simulate_jump_diffusion(S0, mu, sigma, T, M, dt, lambda_j, mu_j, sigma_j))

# Plot the simulated path
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,5))
for path in paths:
    plt.plot(np.linspace(0, T, M), path)
plt.title('Merton Jump Diffusion Model Simulation')
plt.xlabel('Time')
plt.ylabel('Asset Price')
plt.grid()
plt.show()
