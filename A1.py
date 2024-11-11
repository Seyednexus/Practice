import random
n=20
a=[]
for i in range(n):
    a+=[random.random()]
print(a)
#///////////////////////////////////
a=[random.random() for i in range(n)]
print(a)