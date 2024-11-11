import random
value=20
bet=1
best=bet
best_N=0
for bet in range(1,value+1):
   value=100
   N=0
   while(value>0):
         N=N+1
         A=random.randrange(0,2)
         if(A==0):
           if(value-bet >0):
               value=value-bet
           if(value-bet <=0):
               value=0 
         if(A==1):
             value=value+bet
   if(N>best_N):
         best=bet
         best_N=N
print("BEST=",best)