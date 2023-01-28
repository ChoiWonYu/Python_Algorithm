import sys
from itertools import permutations
#dfs 배우고 다시
input=sys.stdin.readline
N=int(input())
num=list(map(int,input().split()))
cont=list(map(int,input().split()))
contarr=[]
for i in range(cont[0]):
    contarr.append('+')
for i in range(cont[1]):
    contarr.append('-')
for i in range(cont[2]):
    contarr.append('*')
for i in range(cont[3]):
    contarr.append('//')
contarr=permutations(contarr,len(contarr))
max=-1000000000
min=1000000000
for i in contarr:
    idx=0
    result=num[0]
    while idx<(len(num)-1):
        if i[idx]=='+':
            result+=num[idx+1]
        elif i[idx]=='-':
            result-=num[idx+1]
        elif i[idx]=='*':
            result*=num[idx+1]
        else:
            if result<0:
                result=-(-result//num[idx+1])
            else:result//=num[idx+1]
        idx+=1
    if result>max:max=result
    if result<min:min=result
print(max)
print(min)

