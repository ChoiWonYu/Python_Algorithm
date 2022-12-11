n=int(input())
c=0
for i in range(1,n+1):
    if i<100:
       c+=1
    else:
        a=list(map(int,str(i)))
        if a[1]*2==a[0]+a[2]:
            c+=1
print(c)