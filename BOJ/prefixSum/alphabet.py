import sys
input=sys.stdin.readline
s=input()
L=len(s)
c=int(input())
result=[[0]*(L+1) for _ in range(26)]
alph=[0]*26
for idx,i in enumerate(s):
    for j in range(26):
        if j==(ord(i)-97):
            alph[j]+=1
        result[j][idx+1]=alph[j]
for _ in range(c):
    a,l,r=input().split()
    l=int(l)
    r=int(r)
    print(result[ord(a)-97][r+1]-result[ord(a)-97][l])

