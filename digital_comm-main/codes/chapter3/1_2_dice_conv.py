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

##Convolution
p_x1=1/6*np.ones((1,6))
p_x2=1/6*np.ones((1,6))
P_px=np.zeros((1,11))
nn1=2
i=0
i1=0
while (nn1<13):
 if nn1<2:
  print("Prob=0")
 elif ((nn1>=2) & (nn1<7)):
  for k in range(1,nn1):
   P_px[0,i]=p_x1[0,nn1-k-1]*p_x2[0,k-1]+P_px[0,i]   
 elif ((nn1>=7) & (nn1<=12)):
  for k in range(nn1-6,7):
   P_px[0,i]=P_px[0,i]+p_x1[0,nn1-k-1]*p_x2[0,k-1] 
   
 nn1=nn1+1
 i=i+1
print(P_px)  

   
#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,P_px, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()# minor

#If using termux
#plt.savefig('figs/pmf.pdf')
plt.savefig('dice2.png')
#subprocess.run(shlex.split("termux-open figs/pmf.pdf"))
#else
plt.show()
