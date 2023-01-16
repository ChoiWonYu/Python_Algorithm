import sys
input=sys.stdin.readline
c=int(input())
for i in range(c):
    jc=int(input())
    d = dict()
    for j in range(jc):

        m,n=input().split()
        if(d.get(n)):d[n]+=1
        else:d[n]=1
    result=1
    for x in d.values():
        result*=(x+1)
    print(result-1)