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
#print(panal)
k=0
y=np.zeros((1,36)).reshape(36,1)
#print(y1[2])
x1=range(1,7)
x2=range(1,7)
for i in x1:
 for j in x2:
  y[k]=i+j
  k=k+1
 
unique1, counts1 = np.unique(y.reshape(1,36), return_counts=True)
prob1=counts1/36
print(prob1)
#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,panal, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()# minor

#If using termux
#plt.savefig('figs/pmf.pdf')
#plt.savefig('dice1.png')
#subprocess.run(shlex.split("termux-open figs/pmf.pdf"))
#else
#plt.show()
