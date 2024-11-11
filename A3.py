a=[1,2,3,4,5]
maximum=a[0]
for v in a[1:]:
    if(v>maximum):
        maximum=v
print(maximum)
#/////////////////////
maximum=max(a)
print(maximum)