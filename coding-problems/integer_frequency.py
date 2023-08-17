arr=[1,4,5,6,6,5,3,5,1,6,4,6]
f={}
for n in arr:
    if n in f:
        f[n]+=1 
    else:
        f[n]=1 
def compare(n):
    return(-f[n],n)
arr=sorted(arr,key=compare)
print(arr)