import math
import numpy as np
x=[[10,2],[2,-5],[-5,5]]
d=[[1,-1,-1],[-1,1,-1],[-1,-1,1]]
P=3
p=1
k=1
E=10
y=[[10,2,-1],[2,-5,-1],[-5,5,-1]]
w=[[1,-2,0],[0,-1,2],[1,3,-1]]
o=[0,0,0]
Emax=0.001
while(E>=Emax):
    E=0
    p=1
    while(p<=P):
        Y=y[p-1]
        D=d[p-1]
        for j in range(0,3):
            net=0
            for i in range (0,3):
                net=net+(w[j][i]*Y[i])
            f=math.exp(-net)
            o[j]=(1-f)/(1+f)
            for i in range (0,3):
                w[j][i]=w[j][i]+((D[j]-o[j])/2)*(1-pow(o[j],2))*Y[i]
            E=E+((D[j]-o[j])*(D[j]-o[j])/2)
        p=p+1
        k=k+1
print('value of k is',k)
print('value of w is')
for i in range(0,3):
    print(w[i])
