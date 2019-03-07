import numpy as np
x=[[0,0],[0,1],[1,0],[1,1]]
d=[-1,1,1,1]
p=1
P=4
k=1
E=10
y=[[0,0,1],[0,1,1],[1,0,1],[1,1,1]]
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
    	if(net>0):
        	o=1
    	elif(net==0):
        	o=D*(-1)
    	else:
        	o=-1
    	for i in range (0,3):
        	w[i]=w[i]+((D-o)/2)*Y[i]
    	E=E+((D-o)*(D-o)/2)
    	p=p+1
    	k=k+1
print("Value of k is",k)
print("Value of w is",w) 


