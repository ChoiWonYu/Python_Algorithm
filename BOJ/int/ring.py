def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

import sys
input=sys.stdin.readline
input()
arr=list(map(int,input().split()))
for i in range(1,len(arr)):
    g=gcd(arr[i],arr[0])
    print(arr[0]//g,end='')
    print('/',end='')
    print(arr[i]//g)

