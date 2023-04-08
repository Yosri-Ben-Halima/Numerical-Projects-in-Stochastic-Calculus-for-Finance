import numpy as np
import matplotlib.pyplot as plt
# Number of samples 
N = 10000
# U1 & U2 ~ U([0,1])
U1 = np.random.uniform(0,1,N)
U2 = np.random.uniform(0,1,N)
# Z1 & Z2 ~ N(0,1)
Z1 = np.sqrt(-np.log(U1))*np.cos(2*np.pi*U2)
Z2 = np.sqrt(-np.log(U1))*np.sin(2*np.pi*U2)
# Standard Gaussian
G = np.random.standard_normal(N)
# Create a figure with subplots for each sample size
fig, axes = plt.subplots(1, 3, figsize=(10, 6))

axes[0].hist(Z1, bins=50, density=True)
axes[0].set_xlabel('Z1')
axes[0].set_ylabel('Density')

axes[1].hist(G, bins=50, density=True)
axes[1].set_xlabel('SDG')

axes[2].hist(Z2, bins=50, density=True)
axes[2].set_xlabel('Z2')

plt.show()

plt.scatter(Z1,Z2,marker='x')
plt.show()
# Estimating the covariance E[Z1*Z2] and the correlation
Cov = (Z1.T).dot(Z2)/N
Cor = (Z1.T).dot(Z2)/(np.sqrt((Z1.T).dot(Z1))*np.sqrt((Z2.T).dot(Z2)))
print(f"The estimated covariance is {Cov} and the correlation is {Cor}")

