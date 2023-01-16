import sys
input=sys.stdin.readline

c=int(input())
for i in range(c):
    n,m=map(int,input().split())
    if m - n == 0:print(1)
    else:
        a,b=0,0;result=1
        for j in range(1,m+1):
            result*=j
            if j==n:a=result
            if j==(m-n):b=result

        print(result//(a*b))