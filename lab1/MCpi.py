import random, math

N=[10,100,1000,4488,10000,30000]
o=[0.5,0.5]
c=[]
for j in N :
    e=0
    for i in range(0,j):
        y=random.random()
        x=random.random()
        d= (math.dist(o,[x,y]))
        if(d<1/2):
            e=e+1
            c.append([x,y])
    res=4*e/j
    print("the result for N=",j," is:" , res ,"\n")

