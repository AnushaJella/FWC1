#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sympy as smp

from scipy.integrate import quad
#if using termux
import subprocess
import shlex
#end if
x=smp.symbols('x')

def f(x,a,b):
  return (x-a)/(b-a)
 
def f1(x,k):
    return x**k
    
a=0;
b=1;    
k=1
dF_x=smp.diff(f(x,a,b));
#mean
fun1=f1(x,k)*dF_x;
mean1=smp.integrate(fun1,(x,a,b));
#variance
fun2=f1(x,2)*dF_x;
ex2=smp.integrate(fun2,(x,a,b));
var=ex2-mean1**2
print(mean1,var)
