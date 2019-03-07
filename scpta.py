import numpy as np
import math
c=1
x=[[0,0],[0,1],[1,0],[1,1],[2,3]]
d=[-1,1,1,1,1]
p=1
P=5
k=1
E=10
lm=1
Emin=0.0001
y=[[0,0,1],[0,1,1],[1,0,1],[1,1,1],[2,3,1]]    #augmented 
w=[-1,-2,-3]     
while (E!=0):
    E=0
    p=1
    while(p<=P):
        Y=y[p-1]
        D=d[p-1]
        net=0
        for i in range (0,3):
            net=net+(w[i]*Y[i])
        
        o=(1-((2.718)**(-net)))/(1+((2.718)**(-net)))
        for i in range (0,3):
            w[i]=w[i]+((D-o)*(1-o*o)/2)*Y[i]
        E=E+((D-o)*(D-o)/2)
        p=p+1
        k=k+1
    if(E<Emin):
        break
print("Value of k is",k)
print("Value of w is",w)
