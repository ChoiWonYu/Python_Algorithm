# n=list(map(int,input()))
# count=1
# if len(n)==2:
#     nCopy=n[1]+n[0]*10
#     n=n[1]*10+sum(n)%10
# else:
#     nCopy=n[0]
#     n=n[0]*10+n[0]
# while nCopy!=n:
#     count+=1
#     n=n%10*10+sum(map(int,str(n)))%10
# print(count)
n=int(input())
count=0
nCopy=n
while 1:
    l=n//10
    r=n%10
    lr=(l+r)%10
    n=r*10+lr
    count+=1
    if nCopy==n:
        break
print(count)


