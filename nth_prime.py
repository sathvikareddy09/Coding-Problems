n=int(input())
i=2
while(True):
    c=0
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            c+=1
    if(c==0):
            n-=1
    if(n==0):
            print(i)
            break
    i+=1