#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy 
#if using termux
import subprocess
import shlex
#end if



x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('T.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
def tri_cdf2(x,a,b,c):
	if (x>a) and (x<=c):
	 return ((x-a)**2)/((b-a)*(c-a))
	 	
def tri_cdf3(x,a,b,c):
	if (x>c) and (x<=b):
	 return 1-((b-x)**2)/((b-a)*(c-a))
	 
def tri_cdf4(x,a,b,c):
	if (x>b):
	 return 1
	 	 	


vec_tri_cdf = np.piecewise(x, [x < 0, ((x >= 0) & (x < 1)), ((x >= 1) & (x < 2)), x >= 2], [0, lambda x: x**2/2, lambda x: 2*x - x**2/2 - 1, 1])	 	 	
#tri_pdf11 = scipy.vectorize(tri_pdf1)
tri_cdf12 = scipy.vectorize(tri_cdf2)
tri_cdf13 = scipy.vectorize(tri_cdf3)
tri_cdf14 = scipy.vectorize(tri_cdf4)	
a=0
b=2
c=1
tri_cdf22=np.piecewise(x,[x<a,((x>=a)&(x<c)),((x>=c)&(x<b)),x>=b],[0,lambda x:((x-a)**2)/((b-a)*(c-a)),lambda x:1-(b-x)**2/((b-a)*(c-a)),1]) 
#plots
plt.plot(x.T,err,'o',label='simulation')#plotting the CDF
#plt.plot(x,tri_cdf12(x,0,2,1),x,tri_cdf13(x,0,2,1),x,tri_cdf14(x,0,2,1))#plotting the CDF
plt.plot(x,tri_cdf22,label='analysis')
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(loc='best')
#if using termux
plt.savefig('./tri_cdf1.pdf')
plt.show()
#plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
