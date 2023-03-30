arr=[1,3,7,8]
k=int(input())
i=1
while(k>0):
    if(i in arr):
        i=i+1
    else:
        k-=1
        i+=1
print(i-1)