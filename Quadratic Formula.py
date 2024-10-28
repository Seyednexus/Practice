import math
a=2
b=4
c=6
discriminant=b*b-4.0*a*c
if discriminant<0:
    print("no real roots")
else:
    d=math.sqrt(discriminant)
    print(((-b+d)/2.0))
    print(((-b-d)/2.0))
