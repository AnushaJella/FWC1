from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import special 
simlen=10000

def coin(x):
	return 2*np.random.randint(2,size=x)-1

X=coin(simlen)
print(X)
#Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
#Simulated probability
psim = counts/simlen
print(psim)

N=np.random.normal(0,1,simlen)
A=5 # this can be changed
temp=0
Y=A*X+N	
#plt.plot(Y,'bx')
#plt.grid()
#plt.show()
