import sympy as sp
n=100
x0=1.0
has=0
x = sp.symbols('x')
def F(x):
    return ((10*x**4)+(53*x**3)+(61*x**2)+(20*x))-57
Ff = sp.diff(F(x), x)
for i in range(1,n+1):
 if(has==0):
    x1=x0-(F(x0)/Ff.subs(x,x0))
    if abs(x1-x0) < 1e-7:
      if( F(x1) < 1e-7 ):
          print("ROOT=",x1)    
          has=1    
    x0=x1
if(has==0):
    print('NOT ROOTS')    
