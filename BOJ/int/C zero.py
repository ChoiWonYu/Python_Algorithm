import sys
input=sys.stdin.readline
def get5count(n):
    count=0
    while n!=0:
        n//=5
        count+=n
    return count
def get2count(n):
    count=0
    while n!=0:
        n//=2
        count+=n
    return count

n,m=map(int,input().split())
print(min(get2count(n)-get2count(n-m)-get2count(m),get5count(n)-get5count(n-m)-get5count(m)))
