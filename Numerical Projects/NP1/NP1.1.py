import numpy as np
import matplotlib.pyplot as plt
# number of samples
N = 10000
# X ~ U([0,1])
X = np.random.uniform(0,1,N)
# number of bins 
nb = 50
# plotting PDF of X
plt.hist(X,bins=nb,range=(0,1),density=True)
plt.title("PDF of X")
plt.xlabel('Value')
plt.ylabel('PDF')
plt.show()
# plotting CDF of X
plt.hist(X,bins=nb,cumulative=True,range=(0,1),density=True)
plt.title("CDF of X")
plt.xlabel('Value')
plt.ylabel('CDF')
plt.show()
# defining X²
X2 = [x**2 for x in X]
# plotting PDF of X²
plt.hist(X2,bins=nb,range=(0,1),density=True)
plt.title("PDF of X²")
plt.xlabel('Value')
plt.ylabel('PDF')
plt.show()
# plotting CDF of X²
plt.hist(X2,bins=nb,cumulative=True,range=(0,1),density=True)
plt.title("CDF of X²")
plt.xlabel('Value')
plt.ylabel('CDF')
plt.show()