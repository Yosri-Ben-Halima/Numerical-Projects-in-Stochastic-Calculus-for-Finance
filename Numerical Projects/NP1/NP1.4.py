import matplotlib.pylab as plb
# Number of samples
N = 10000
# Cauchy dist
C = plb.standard_cauchy(N) 
# Gaussian dist
G = plb.standard_normal(N)
# Plot histograms of the empirical means
fig, axes = plb.subplots(1, 2, figsize=(15, 5))
axes[0].hist(C, bins=100, range=(-10,10), density=True)
axes[0].set_title("PDF of SD Cauchy")
axes[1].hist(G, bins=100, range=(-10,10), density=True)
axes[1].set_title("PDF of SD Gaussian")
plb.show()
# Calculate empirical mean
S = plb.cumsum(C)/plb.arange(1, N+1)
# Calculate true mean
true_mean = plb.mean(C)
# Plot the empirical mean as a function of the sample size
plb.plot(plb.arange(1, N+1), S)
plb.hlines(true_mean, 1, N, colors='red', linestyles='dashed')
plb.xlabel('Sample size')
plb.ylabel('Empirical mean')
plb.show()
# Define a function  that returns the empirical mean
def Empirical_Mean(n):
    global N
    Nn = plb.standard_cauchy(size=(n, N))
    return Nn,plb.mean(Nn,axis=1)
# Plot histograms of the empirical means
fig, axes = plb.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(Empirical_Mean(100)[1], bins=50, density=True)
axes[0, 0].set_title("PDF for N=10")

axes[0, 1].hist(Empirical_Mean(100)[1], bins=50, cumulative=True, density=True)
axes[0, 1].set_title("CDF for N=10")

axes[1, 0].hist(Empirical_Mean(1000)[1], bins=50, density=True)
axes[1, 0].set_title("PDF for N=100")

axes[1, 1].hist(Empirical_Mean(1000)[1], bins=50, cumulative=True, density=True)
axes[1, 1].set_title("CDF for N=100")

plb.show()
