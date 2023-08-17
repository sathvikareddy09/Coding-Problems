n=input().split()
print(n)
count=0
for i in n:
    a=0
    for l in i:
        if l=="a" or l=="e" or l=="i" or l=="o" or l=="u":
            a+=1 
    if a%2==0:
        count+=2
    else:
        count+=1 
print(count)