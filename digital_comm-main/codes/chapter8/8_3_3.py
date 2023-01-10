import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

sigma = 1
mean = 0
num_samples = 1000000
n1 = np.random.normal(mean, sigma, num_samples)
n2 = np.random.normal(mean, sigma, num_samples)
X = n2-n1
Y = -n2-n1
p = np.mean((X-np.mean(X))*(Y-np.mean(Y)))/np.sqrt(np.var(X)*np.var(Y))
print("Correlation coefficient is:",p)

plt.scatter(X[0:7000],Y[0:7000],s=10)
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")

plt.savefig('X_y_scatter.pdf')

plt.show() 
