
import matplotlib.pyplot as plt
import numpy as np
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # diagonal covariance
A_db=5 # this can be changed
A=10**(0.1*A_db)
simlen = int(1000)

def coin(x):
	return 2*np.random.randint(2,size=x)-1
	
X=coin(simlen)	
n1, n2 = np.random.multivariate_normal(mean, cov, simlen).T

y1 = n1
y2 = A*X + n2
x=np.linspace(-10,10,len(y2))

plt.scatter(x, y2)
#plt.legend(['$\mathbf{x} = \mathbf{s}_0$','$\mathbf{x} = \mathbf{s}_1$'])
plt.xlabel("$x$")
plt.ylabel("$Y$")
plt.savefig('Y_scatter5.pdf')
plt.show()
