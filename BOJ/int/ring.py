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
    print("{0}/{1}".format(arr[0]//g,arr[i]//g))

