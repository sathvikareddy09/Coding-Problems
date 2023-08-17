import math
arr=[9,-9,11,12,19,14,-10,14,-9,13]
c=0;
for i in arr:
    if i<0:
        continue
    else:
        a=int(math.sqrt(i))
        if a*a==i:
            c=c+1
print(c)