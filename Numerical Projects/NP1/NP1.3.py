import numpy as np
import matplotlib.pyplot as plt
# sample size
N = 10000
# Y_N
def Y(Ni,ax=0):
    global N
    S = np.random.exponential(scale=1, size=(Ni,N))
    Sn = np.sum(S,axis=ax)
    return (Sn-Ni)/np.sqrt(Ni)
# SGD sampling
G = np.random.standard_normal(N)
# Plot histograms of the empirical means
fig, axes = plt.subplots(1, 2, figsize=(12, 8))

#axes[0].hist(Y(100), bins=50, density=True)
#axes[0].set_title("PDF for N=100")

axes[0].hist(G, bins=50, density=True)
axes[0].set_title("PDF of SDG")

axes[1].hist(Y(10000), bins=50, density=True)
axes[1].set_title("PDF for N=10000")

plt.show()

