import sys
from itertools import combinations
input=sys.stdin.readline
startLink=[]
N=int(input())
for i in range(N):
    startLink.append(list(map(int,input().split())))

team=[i for i in range(N)]
teams=list(combinations(team,N//2))
min=1000000000000
total=len(teams)
for i in range(total):
    if i==total//2:break
    start=0
    link=0
    oth=teams[-(i+1)]
    startT=teams[i]
    for j in range(N//2):
        for m in range(N//2):
            if m!=j:
                start+=startLink[startT[j]][startT[m]]
                link+=startLink[oth[j]][oth[m]]
    if (start-link)<0:
        if link-start<min:min=link-start
    else:
        if start-link<min:min=start-link
print(min)
