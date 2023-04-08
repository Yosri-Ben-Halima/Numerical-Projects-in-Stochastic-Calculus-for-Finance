import numpy as np
import matplotlib.pyplot as plt

# Number of samples 
N = 10000
# Generate N exponentially distributed random numbers with parameter 1
X = np.random.exponential(scale=1, size=N)
# Calculate empirical mean
S = np.cumsum(X)/np.arange(1, N+1)
# Calculate true mean
true_mean = np.mean(X)
# Plot the empirical mean as a function of the sample size
plt.plot(np.arange(1, N+1), S)
plt.hlines(true_mean, 1, N, colors='red', linestyles='dashed')
plt.xlabel('Sample size')
plt.ylabel('Empirical mean')
plt.show()
# Define a function  that returns the empirical mean
def Empirical_Mean(n):
    Nn = np.random.exponential(scale=1, size=(n, 10000))
    return Nn,np.mean(Nn,axis=0)
# Plot histograms of the empirical means
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(Empirical_Mean(100)[1], bins=50, density=True)
axes[0, 0].set_title("PDF for N=100")

axes[0, 1].hist(Empirical_Mean(100)[1], bins=50, cumulative=True, density=True)
axes[0, 1].set_title("CDF for N=100")

axes[1, 0].hist(Empirical_Mean(10000)[1], bins=50, density=True)
axes[1, 0].set_title("PDF for N=10000")

axes[1, 1].hist(Empirical_Mean(10000)[1], bins=50, cumulative=True, density=True)
axes[1, 1].set_title("CDF for N=10000")

plt.show()

#lim Sn/n when (n->+inf) ~ N(1,sigma²)

