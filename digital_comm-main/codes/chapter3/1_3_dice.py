import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

#Sample size
simlen = 10000
#Possible outcomes
n = range(2,13)
# Generate X1 and X2
y = np.random.randint(1,7, size=(2, simlen))
# unit step function
def step(x):
    return 1*(x>=0)

#Generate X
X = np.sum(y, axis = 0) 

#Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
#Simulated probability
psim = counts/simlen

#Theoretical probability
n1 = range(2,8)
n2 = range(8,13)
panal1 = (n1 -np.ones((1,6)))
panal2 = (13*np.ones((1,5))-n2)
panal = np.concatenate((panal1,panal2),axis=None)/36

##Z-transform
ts=np.arange(1,12,1)
step_sig1=step(ts-1)
n11=(n-np.ones((1,11)))*step_sig1
n12=(n-7*np.ones((1,11)))*step(ts-7)
n13=(n-13*np.ones((1,11)))*step(ts-13)
panal_z=(n11-2*n12+n13)/36
print(panal_z)

#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,panal_z, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()# minor

#If using termux
#plt.savefig('figs/pmf.pdf')
plt.savefig('dice3.png')
#subprocess.run(shlex.split("termux-open figs/pmf.pdf"))
#else
plt.show()
