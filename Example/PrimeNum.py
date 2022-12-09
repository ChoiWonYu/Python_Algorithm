import math
s,l=input().split()
s=int(s)
l=int(l)
#s,l=map(int,input().split())
arr=[True for i in range(l+1)]
#array[1]=0
for i in range(2,int(math.sqrt(l))+1):
    j=2
    if arr[i]==True:
        while i*j<=l:
            arr[i*j]=False
            j+=1

for i in range(s,l+1):
    if arr[i]==True:
    #if arr[i]:
        print(i)


